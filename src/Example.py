#Example usage of the text formatting functions
from text_formatter import *

text = "<p>Some <b>bold</b> and <i>italicized</i> text with <u>underline</u> and <s>strikethrough</s> formatting.</p>"
print("Original text:")
print(text)
print()

#Remove HTML tags
clean_text = remove_html_tags(text)
print("Text with HTML tags removed:")
print(clean_text)
print()

#Remove punctuation
no_punc_text = remove_punctuation(text)
print("Text with punctuation removed:")
print(no_punc_text)
print()

#Replace with synonyms
synonym_text = replace_with_synonyms(text)
print("Text with synonyms replaced:")
print(synonym_text)
print()

#Make heading
heading_text = make_heading("This is a heading", 2)
print("Text formatted as a heading:")
print(heading_text)
print()

#Make italics
italic_text = make_italics("This is italicized")
print("Text formatted as italic:")
print(italic_text)
print()

#Make bold
bold_text = make_bold("This is bold")
print("Text formatted as bold:")
print(bold_text)
print()

#Make underline
underline_text = make_underline("This is underlined")
print("Text formatted as underlined:")
print(underline_text)
print()

#Make strikethrough
strikethrough_text = make_strikethrough("This is strikethrough")
print("Text formatted as strikethrough:")
print(strikethrough_text)
print()

#Make colored
colored_text = make_colored("This is colored", "blue")
print("Text formatted as colored:")
print(colored_text)
print()

#Make uppercase
uppercase_text = make_uppercase("This is uppercase")
print("Text formatted as uppercase:")
print(uppercase_text)
print()

#Make lowercase
lowercase_text = make_lowercase("THIS IS LOWERCASE")
print("Text formatted as lowercase:")
print(lowercase_text)
print()

#Make capitalized
capitalized_text = make_capitalized("this is capitalized")
print("Text formatted as capitalized:")
print(capitalized_text)
print()

#Make reversed
reversed_text = make_reversed("This is reversed")
print("Text reversed:")
print(reversed_text)
print()