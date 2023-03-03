def make_text_bigger(text, size):
    """Increase the font size of the text.

    Args:
        text (str): The text to modify.
        size (int): The new font size.

    Returns:
        str: The modified text.
    """
    return f'<h{size}>{text}</h{size}>'

def make_text_italics(text):
    """Add italics formatting to the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return f'<i>{text}</i>'

def make_text_bold(text):
    """Add bold formatting to the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return f'<b>{text}</b>'

def make_text_underline(text):
    """Add underline formatting to the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return f'<u>{text}</u>'

def make_text_strikethrough(text):
    """Add strikethrough formatting to the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return f'<s>{text}</s>'

def make_text_colored(text, color):
    """Add colored formatting to the text.

    Args:
        text (str): The text to modify.
        color (str): The color to apply.

    Returns:
        str: The modified text.
    """
    return f'<span style="color:{color}">{text}</span>'

def make_text_uppercase(text):
    """Convert text to uppercase.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return text.upper()

def make_text_lowercase(text):
    """Convert text to lowercase.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return text.lower()

def make_text_capitalized(text):
    """Capitalize the first letter of each word in the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return text.title()

def make_text_reversed(text):
    """Reverse the order of characters in the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text.
    """
    return text[::-1]