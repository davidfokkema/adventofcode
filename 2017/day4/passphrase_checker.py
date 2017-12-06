import itertools


def is_valid(passphrase):
    words = passphrase.split(' ')
    for n, word in enumerate(words):
        if word in words[:n]:
            return False
    return True


def is_secure(passphrase):
    words = passphrase.split(' ')
    for n, word in enumerate(words):
        anagrams = [''.join(u) for u in itertools.permutations(word,
                                                               len(word))]
        for anagram in anagrams:
            if anagram in words[:n]:
                return False
    return True


def count_valid_passphrases(filename):
    sum = 0
    with open(filename) as f:
        for passphrase in f.readlines():
            if is_valid(passphrase.rstrip()):
                sum += 1
    return sum


def count_secure_passphrases(filename):
    sum = 0
    with open(filename) as f:
        for passphrase in f.readlines():
            if is_secure(passphrase.rstrip()):
                sum += 1
    return sum


if __name__ == '__main__':
    print('Day 4, part 1:', count_valid_passphrases('input.txt'))
    print('Day 4, part 2:', count_secure_passphrases('input.txt'))
