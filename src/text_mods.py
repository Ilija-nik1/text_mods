import re
import string
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize
from nltk.tree import Tree
from googletrans import Translator
from gensim.summarization.summarizer import summarize
from functools import lru_cache
from typing import List
from collections import Counter
import random
import spacy

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')

def get_synonyms(word: str, method: str) -> List[str]:
    """Get a list of synonyms for a given word."""
    synonyms: List[str] = []
    if method == "synonyms":
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                if lemma.name() not in synonyms and lemma.name() != word:
                    synonyms.append(lemma.name())
    elif method == "stemming":
        base_word = stemmer.stem(word)
        for syn in wordnet.synsets(base_word):
            for lemma in syn.lemmas():
                if lemma.name() not in synonyms and lemma.name() != base_word:
                    synonyms.append(lemma.name())
    elif method == "lemmatization":
        pos = nltk.pos_tag([word])[0][1][0].lower()
        base_word = lemmatizer.lemmatize(word, pos=pos)
        for syn in wordnet.synsets(base_word):
            for lemma in syn.lemmas():
                if lemma.name() not in synonyms and lemma.name() != base_word:
                    synonyms.append(lemma.name())
    return synonyms

def remove_html_tags(text: str) -> str:
    """Remove HTML tags from a given text string."""
    html_pattern = re.compile('<.*?>')
    return re.sub(html_pattern, '', text)

def remove_punctuation(text: str) -> str:
    """Remove punctuation from a given text string."""
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def replace_with_first_synonym(text: str) -> str:
    """Replace words in a given text with their first synonym."""
    tokens = nltk.word_tokenize(text)
    new_text = [get_synonyms(token)[0] if get_synonyms(token) else token for token in tokens]
    return ' '.join(new_text)

def replace_with_random_synonym(text: str, method: str) -> str:
    """Replace words in a given text with a random synonym."""
    tokens = nltk.word_tokenize(text)
    new_text = [random.choice(get_synonyms(token, method)) if get_synonyms(token, method) else token for token in tokens]
    return ' '.join(new_text)

def count_word_frequencies(text: str) -> Counter:
    """Count the frequency of each word in a given text string."""
    tokens = nltk.word_tokenize(text)
    return Counter(tokens)

def remove_stopwords(text: str) -> str:
    """Remove stopwords from a given text string."""
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    filtered_text = [token for token in tokens if token.lower() not in stop_words]
    return ' '.join(filtered_text)

def summarize_text(text: str) -> str:
    """Summarize a given text string."""
    return summarize(text)

def extract_entities(text: str) -> List[str]:
    """Extract named entities from a given text string."""
    chunks = ne_chunk(pos_tag(word_tokenize(text)))
    entities = []
    for chunk in chunks:
        if isinstance(chunk, Tree) and chunk.label() in ['PERSON', 'ORGANIZATION', 'GPE']:
            entities.append(' '.join([token for token, pos in chunk]))
    return entities

def make_heading(text: str, size: int) -> str:
    """Increase the font size of the text."""
    return f'<h{size}>{text}</h{size}>'

def make_italics(text: str) -> str:
    """Add italics formatting to the text."""
    return f'<i>{text}</i>'

def make_bold(text: str) -> str:
    """Add bold formatting to the text."""
    return f'<b>{text}</b>'

def make_underline(text: str) -> str:
    """Add underline formatting to the text."""
    return f'<u>{text}</u>'

def make_strikethrough(text: str) -> str:
    """Add strikethrough formatting to the text."""
    return f'<s>{text}</s>'

def make_colored(text: str, color: str) -> str:
    """Add colored formatting to the text."""
    return f'<span style="color:{color}">{text}</span>'

def make_uppercase(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

def make_lowercase(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()

def make_capitalized(text: str) -> str:
    """Capitalize the first letter of each word in the text."""
    return text.title()

def make_reversed(text: str) -> str:
    """Reverse the order of characters in the text."""
    return text[::-1]