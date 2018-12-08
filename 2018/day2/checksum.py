def has_letter_twice(string):
    return has_letter_n_times(2, string)


def has_letter_thrice(string):
    return has_letter_n_times(3, string)


def has_letter_n_times(n, string):
    letters = set(string)
    for letter in letters:
        if string.count(letter) == n:
            return True
    return False


def calculate_checksum(strings):
    count_twice = 0
    count_thrice = 0

    for string in strings:
        if has_letter_twice(string):
            count_twice += 1

    for string in strings:
        if has_letter_thrice(string):
            count_thrice += 1

    return count_twice * count_thrice


if __name__ == '__main__':
    with open('input.txt') as f:
        strings = f.readlines()
    checksum = calculate_checksum(strings)

    print(f"Day 2, part 1: checksum is {checksum}")
