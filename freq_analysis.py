from collections import Counter
from auxiliary import clean_text
from config import LETTER_FREQUENCIES

def split_by_key_length(ciphertext, key_length):
    segments = [''] * key_length
    index = 0
    for char in ciphertext:
        if char.isalpha():
            segments[index % key_length] += char
            index += 1
    return segments



def frequency_analysis(text):
    text = ''.join([c.upper() for c in text if c.isalpha()])
    counter = Counter(text)
    total = sum(counter.values())
    freq = {}
    for letter in sorted(counter):
        freq[letter] = counter[letter] / total
    return freq

def find_shift(segment):
    best_shift = 0
    best_score = float('inf')

    for shift in range(26):
        decrypted = ""

        for c in segment:
            decrypted += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))

        counter = Counter(decrypted)
        total = sum(counter.values())

        score = 0

        for letter in LETTER_FREQUENCIES:
            observed = counter.get(letter, 0) / total
            expected = LETTER_FREQUENCIES[letter] / 100

            score += (observed - expected) ** 2

        if score < best_score:
            best_score = score
            best_shift = shift

    return best_shift


def caesar_find_shift(ciphertext):
    segment = clean_text(ciphertext)
    shift = find_shift(segment)
    return shift

def recover_key(ciphertext, key_length):
    ciphertext = clean_text(ciphertext)
    segments = split_by_key_length(ciphertext, key_length)

    key = ""

    for segment in segments:
        shift = find_shift(segment)
        key += chr(shift + ord('A'))

    return key