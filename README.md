Introduction

This code provides a set of functions to perform text processing tasks. These tasks include removing HTML tags and punctuation, replacing words with their synonyms, and formatting text with different styles such as bold, italic, and more.

Functions

remove_html_tags(text: str) -> str
This function removes HTML tags from a given text string.

remove_punctuation(text: str) -> str
This function removes punctuation from a given text string.

replace_with_first_synonym(text: str) -> str
This function replaces words in a given text with their first synonym.

make_heading(text: str, size: int) -> str
This function increases the font size of the text by creating a heading with the specified size (1 to 6).

make_italics(text: str) -> str
This function adds italics formatting to the text.

make_bold(text: str) -> str
This function adds bold formatting to the text.

make_underline(text: str) -> str
This function adds underline formatting to the text.

make_strikethrough(text: str) -> str
This function adds strikethrough formatting to the text.

make_colored(text: str, color: str) -> str
This function adds colored formatting to the text by specifying the color as a string in HTML format (e.g., "red", "#FF0000").

make_uppercase(text: str) -> str
This function converts text to uppercase.

make_lowercase(text: str) -> str
This function converts text to lowercase.

make_capitalized(text: str) -> str
This function capitalizes the first letter of each word in the text.

make_reversed(text: str) -> str
This function reverses the order of characters in the text.

Dependencies

This code requires the following dependencies:

re
string
nltk
nltk.corpus.wordnet
functools.lru_cache