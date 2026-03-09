# level 1
def extend_key(text, key):
    key = key.upper()  # keeping the key in upper registry
    extended_key = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            extended_key += key[key_index % len(key)]
            key_index += 1
        else:
            extended_key += char
    return extended_key


def encrypt_vigenere(text, key):
    key = extend_key(text, key)
    cipher_text = ""

    for i in range(len(text)):
        char = text[i]
        k = key[i]
        if char.isupper():
            x = (ord(char) - ord('A') + ord(k) - ord('A')) % 26
            cipher_text += chr(x + ord('A'))
        elif char.islower():
            x = (ord(char) - ord('a') + ord(k) - ord('A')) % 26
            cipher_text += chr(x + ord('a'))
        else:
            cipher_text += char

    return cipher_text


def decrypt_vigenere(cipher_text, key):
    key = extend_key(cipher_text, key)
    original_text = ""

    for i in range(len(cipher_text)):
        char = cipher_text[i]
        k = key[i]
        if char.isupper():
            x = (ord(char) - ord('A') - (ord(k) - ord('A')) + 26) % 26
            original_text += chr(x + ord('A'))
        elif char.islower():
            x = (ord(char) - ord('a') - (ord(k) - ord('A')) + 26) % 26
            original_text += chr(x + ord('a'))
        else:
            original_text += char

    return original_text



