# Text Formatting Toolkit

text_mods is a Python module for formatting text strings in various ways. It includes functions for removing HTML tags and punctuation, replacing words with synonyms, and applying different formatting styles such as bold, italic, and colored text.

## Requirements+

* Python 3.6 or higher
* NLTK library
* WordNet database

## Installation

* Install Python 3.6 or higher from the official website: [Here] (<https://www.python.org/downloads/>)
* Install the NLTK library by running pip install nltk in your terminal or command prompt.
* Download the WordNet database by running the following commands in a Python interpreter:
arduino

``` Python
import nltk
nltk.download('wordnet')
```

* Download or clone the code from the Github repository: [GitHub] (<https://github.com/Ilija-nik1/text_mods>)

### Clone

Clone the repository using git:

```bash
git clone https://github.com/Ilija-nik1/text_mods.git
```

## Usage

Here are some examples of how to use the functions in the module

``` Python
from text_mods import *

text = '<h1>Hello, world!</h1>'
text = remove_html_tags(text)
text = make_bold(text)
print(text)  # <b>Hello, world!</b>

text = 'This is a sample sentence.'
text = replace_with_first_synonym(text)
text = make_colored(text, 'red')
print(text)  # <span style="color:red">This is a sampling sentence.</span>
```

For more information on each function, please refer to the docstrings in the code.

## Contributing

If you find any bugs or have suggestions for new features, please open an issue or pull request on the Github repository.

## License

This code is licensed under the MIT License.