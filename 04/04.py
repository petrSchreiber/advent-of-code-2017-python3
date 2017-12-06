from collections import Counter

def is_correct(passphrase):
    words = passphrase.split(' ')

    results = Counter(words)

    max_occurences = results.most_common(1)
    return True if max_occurences[0][1] == 1 else False


with open('data.txt', 'r') as f:
    passphrases = f.read().splitlines()

total = 0
for passphrase in passphrases:
    if is_correct(passphrase):
        total += 1

print(total)
