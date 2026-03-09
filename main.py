from cipher_caesar import caesar_decrypt, caesar_encrypt
from cipher_vigenere import encrypt_vigenere, decrypt_vigenere
from kasiski import kasiski_examination, kasiski_key_length
from freq_analysis import recover_key, frequency_analysis, caesar_find_shift

from config import text_example, KEY_VIGENERE, CAESAR_SHIFT




def task1():
    print("--- Caesar")
    text = text_example
    encrypted_text = caesar_encrypt(text, CAESAR_SHIFT)
    print("Encrypted: ", encrypted_text)
    freq = frequency_analysis(encrypted_text)
    print("Frequency: ", freq)

    detected_shift = caesar_find_shift(encrypted_text)
    print("Detected shift: ", detected_shift)
    
    decrypted_text = caesar_decrypt(encrypted_text, detected_shift)
    print("Decrypted: ", decrypted_text)


def task2():
    print("--- Vigenere")
    text = text_example
    key = KEY_VIGENERE
    
    encrypted_text = encrypt_vigenere(text, key)
    print("Encrypted: ", encrypted_text)

    distances = kasiski_examination(encrypted_text)
    key_length = kasiski_key_length(distances)
    print("Estimated key length: ", key_length)

    recovered_key = recover_key(encrypted_text, key_length)
    print("Recovered key: ", recovered_key)
    decrypted = decrypt_vigenere(encrypted_text, recovered_key)
    print("Decrypted: ", decrypted)
    
task1()
task2()