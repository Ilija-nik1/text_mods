import re
import string
import random
from typing import List
from collections import Counter

import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

from transformers import pipeline
from googletrans import Translator
from functools import lru_cache

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

STOPWORDS_LANGUAGE = 'english'

@lru_cache(maxsize=None)
def get_synonyms(word: str, method: str) -> List[str]:
    synonyms = set()
    if method == "synonyms":
        for syn in wordnet.synsets(word):
            synonyms.update(lemma.name() for lemma in syn.lemmas() if lemma.name() != word)
    elif method == "stemming":
        base_word = stemmer.stem(word)
        for syn in wordnet.synsets(base_word):
            synonyms.update(lemma.name() for lemma in syn.lemmas() if lemma.name() != base_word)
    elif method == "lemmatization":
        pos = pos_tag([word])[0][1][0].lower()
        base_word = lemmatizer.lemmatize(word, pos=pos)
        for syn in wordnet.synsets(base_word):
            synonyms.update(lemma.name() for lemma in syn.lemmas() if lemma.name() != base_word)
    return list(synonyms)

def remove_html_tags(text: str) -> str:
    html_pattern = re.compile('<.*?>')
    return re.sub(html_pattern, '', text)

def remove_punctuation(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def replace_with_first_synonym(text: str) -> str:
    tokens = nltk.word_tokenize(text)
    new_text = [get_synonyms(token)[0] if get_synonyms(token) else token for token in tokens]
    return ' '.join(new_text)

def replace_with_random_synonym(text: str, method: str) -> str:
    tokens = nltk.word_tokenize(text)
    new_text = [random.choice(get_synonyms(token, method)) if get_synonyms(token, method) else token for token in tokens]
    return ' '.join(new_text)

def count_word_frequencies(text: str) -> Counter:
    tokens = nltk.word_tokenize(text)
    return Counter(tokens)

def remove_stopwords(text: str) -> str:
    stop_words = set(stopwords.words(STOPWORDS_LANGUAGE))
    tokens = nltk.word_tokenize(text)
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
