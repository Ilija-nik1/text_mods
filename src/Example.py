from text_mods import *

text = '<h1>Hello, world!</h1>'
text = remove_html_tags(text)
text = make_bold(text)
print(text)  # <b>Hello, world!</b>

text = 'This is a sample sentence.'
text = replace_with_first_synonym(text)
text = make_colored(text, 'red')
print(text)  # <span style="color:red">This is a sampling sentence.</span>