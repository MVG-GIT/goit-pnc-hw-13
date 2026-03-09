# level 2 - Kasiski
from collections import Counter

from auxiliary import clean_text

def kasiski_examination(ciphertext):
    ciphertext = clean_text(ciphertext)
    seq_distances = []
    for i in range(len(ciphertext) - 3):
        seq = ciphertext[i:i+3]
        for j in range(i+3, len(ciphertext) - 3):
            if ciphertext[j:j+3] == seq:
                seq_distances.append(j - i)

    return seq_distances

def get_factors(n):
    factors = []
    for i in range(2, min(n, 20)):  # key length limit
        if n % i == 0:
            factors.append(i)
    return factors


def kasiski_key_length(distances):
    all_factors = []

    for d in distances:
        all_factors.extend(get_factors(d))

    counter = Counter(all_factors)

    if not counter:
        return None

    print("Possible key lengths:")
    for length, freq in counter.most_common(5):
        print(f"Length [{length}]: {freq} times")

    return counter.most_common(1)[0][0]