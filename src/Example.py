#Usag: To use these functions, you need to import the code and call the desired function with the appropriate parameters. For example:
#Make sure to have all the dependencies installed before using these functions.
import text_mods

text = "This is an example text."
text = text_processing.remove_html_tags(text)
text = text_processing.remove_punctuation(text)
text = text_processing.replace_with_first_synonym(text)
text = text_processing.make_bold(text)
print(text)
#This will output: "This is an exemplar school text."