def clean_text(text):
    return ''.join(c for c in text.upper() if c.isalpha())