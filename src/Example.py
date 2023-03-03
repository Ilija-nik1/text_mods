import text_mods

text = 'Hello, world!'
modified_text = text_mods.make_text_bigger(text, 2)
modified_text = text_mods.make_text_italics(modified_text)
modified_text = text_mods.make_text_bold(modified_text)
modified_text = text_mods.make_text_underline(modified_text)
modified_text = text_mods.make_text_strikethrough(modified_text)
modified_text = text_mods.make_text_colored(modified_text, 'blue')
modified_text = text_mods.make_text_uppercase(modified_text)
modified_text = text_mods.make_text_lowercase(modified_text)
modified_text = text_mods.make_text_capitalized(modified_text)
modified_text = text_mods.make_text_reversed(modified_text)

print(modified_text)
# Output: !DLROW ,OLLEH</H2></I></B></U></S></SPAN>