import re
import string
import nltk
from nltk.corpus import wordnet
from functools import lru_cache
from typing import List

def get_synonyms(word: str) -> List[str]:
    """Get a list of synonyms for a given word."""
    synonyms: List[str] = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.name() not in synonyms and lemma.name() != word:
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