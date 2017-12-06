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


# This is what I should have thought of. I was too busy writing tests and
# almost literally implementing the logic of the puzzle's description. Of
# course, Tom Kooij did think of this. While the following solution is less
# verbose than the one above, the logic is not hard to follow. I like it.
#
# def is_valid(passphrase):
#     words = passphrase.split(' ')
#     # the set throws out duplicates
#     return len(words) == len(set(words))
#
#
# def is_secure(passphrase):
#     words = passphrase.split(' ')
#     # by sorting the letters in a word, anagrams become identical
#     sorted_words = [''.join(sorted(u)) for u in words]
#     # again, check for duplicates
#     return len(sorted_words) == len(set(sorted_words))


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
