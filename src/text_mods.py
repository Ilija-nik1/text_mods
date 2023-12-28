import re
import string
import random
from typing import List
from collections import Counter

import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree
from functools import lru_cache

from transformers import pipeline
from googletrans import Translator
from textblob import TextBlob

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

STOPWORDS_LANGUAGE = 'english'
stopwords = set(stopwords.words(STOPWORDS_LANGUAGE))

def pre_load_stopwords():
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

pre_load_stopwords()

@lru_cache(maxsize=None)
def get_synonyms(word: str, method: str, stopwords: set) -> list:
    synonyms = set()

    def get_synonyms_for_word(word):
        for syn in wordnet.synsets(word):
            synonyms.update(lemma.name() for lemma in syn.lemmas() if lemma.name() != word)

    methods = {
        "synonyms": get_synonyms_for_word,
        "stemming": lambda word: get_synonyms_for_word(stemmer.stem(word)),
        "lemmatization": lambda word: get_synonyms_for_word(lemmatizer.lemmatize(word, pos=pos_tag([word])[0][1][0].lower()))
    }

    method_func = methods.get(method)
    if method_func:
        method_func(word)

    return list(synonyms)

def remove_html_tags(text: str) -> str:
    html_pattern = re.compile('<.*?>')
    return re.sub(html_pattern, '', text)

def remove_punctuation(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def replace_with_first_synonym(text: str) -> str:
    tokens = word_tokenize(text)
    new_text = [get_synonyms(token)[0] if get_synonyms(token) else token for token in tokens]
    return ' '.join(new_text)

def replace_with_random_synonym(text: str, method: str) -> str:
    tokens = word_tokenize(text)
    new_text = [random.choice(get_synonyms(token, method)) if get_synonyms(token, method) else token for token in tokens]
    return ' '.join(new_text)

def count_word_frequencies(text: str) -> Counter:
    tokens = word_tokenize(text)
    return Counter(tokens)

def remove_stopwords(text: str) -> str:
    stop_words = set(stopwords.words(STOPWORDS_LANGUAGE))
    tokens = word_tokenize(text)
    filtered_text = [token for token in tokens if token.lower() not in stop_words]
    return ' '.join(filtered_text)

def summarize_text(text: str) -> str:
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary']

def extract_entities(text: str) -> List[str]:
    chunks = ne_chunk(pos_tag(word_tokenize(text)))
    entities = [' '.join([token for token, pos in chunk]) for chunk in chunks if isinstance(chunk, Tree) and chunk.label() in ['PERSON', 'ORGANIZATION', 'GPE']]
    return entities

def make_heading(text: str, size: int) -> str:
    return f'<h{size}>{text}</h{size}>'

def make_italics(text: str) -> str:
    return f'<i>{text}</i>'

def make_bold(text: str) -> str:
    return f'<b>{text}</b>'

def make_underline(text: str) -> str:
    return f'<u>{text}</u>'

def make_strikethrough(text: str) -> str:
    return f'<s>{text}</s>'

def make_colored(text: str, color: str) -> str:
    return f'<span style="color:{color}">{text}</span>'

def make_uppercase(text: str) -> str:
    return text.upper()

def make_lowercase(text: str) -> str:
    return text.lower()

def make_capitalized(text: str) -> str:
    return text.title()

def make_reversed(text: str) -> str:
    return text[::-1]

translator = Translator()

def translate_text(text: str, src_lang: str, dest_lang: str) -> str:
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def detect_language(text: str) -> str:
    detection = translator.detect(text)
    return detection.lang

def tokenize_sentences(text: str) -> List[str]:
    sentences = sent_tokenize(text)
    return sentences

def tokenize_words(text: str) -> List[str]:
    words = word_tokenize(text)
    return words

def remove_numbers(text: str) -> str:
    text_without_numbers = re.sub(r'\d+', '', text)
    return text_without_numbers

def safe_translate(text, src_lang, dest_lang):
    try:
        return translate_text(text, src_lang, dest_lang)
    except Exception as e:
        print(f"Error in translation: {e}")
        return text

def correct_spelling(text: str) -> str:
    corrected_text = TextBlob(text).correct()
    return str(corrected_text)

def analyze_sentiment(text: str) -> float:
    sentiment = TextBlob(text).sentiment.polarity
    return sentiment

def extract_keywords(text: str, num_keywords: int = 5) -> List[str]:
    blob = TextBlob(text)
    return [item[0] for item in blob.np_counts.most_common(num_keywords)]