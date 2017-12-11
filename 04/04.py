from collections import Counter


def is_correct(passphrase, allow_permutations=True):
    words = passphrase.split(' ')

    if not allow_permutations:
        words = [''.join(sorted(word)) for word in words]

    results = Counter(words)

    max_occurrences = results.most_common(1)
    return True if max_occurrences[0][1] == 1 else False


def count_valid_passphrases(passphrases, allow_permutations=True):
    total = 0
    for passphrase in passphrases:
        if is_correct(passphrase, allow_permutations):
            total += 1

    return total


with open('data.txt', 'r') as f:
    passphrases = f.read().splitlines()

print(count_valid_passphrases(passphrases))
print(count_valid_passphrases(passphrases, allow_permutations=False))
