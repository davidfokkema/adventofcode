def is_valid(passphrase):
    words = passphrase.split(' ')
    for n, word in enumerate(words):
        if word in words[:n]:
            return False
    return True


def count_valid_passphrases(filename):
    sum = 0
    with open(filename) as f:
        for passphrase in f.readlines():
            if is_valid(passphrase.rstrip()):
                sum += 1
    return sum
