def is_valid(passphrase):
    words = passphrase.split(' ')
    for n, word in enumerate(words):
        if word in words[:n]:
            return False
    return True

