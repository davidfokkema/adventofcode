def find_common_letters_in_two_strings(s1, s2):
    N = len(s1)
    for idx in range(N):
        if s1[idx] != s2[idx]:
            cut_s1 = s1[:idx] + s1[idx + 1:]
            cut_s2 = s2[:idx] + s2[idx + 1:]
            if cut_s1 == cut_s2:
                return cut_s1
    return None


def find_common_letters(string_list):
    for idx, string in enumerate(string_list):
        for string2 in string_list[idx + 1:]:
            common_letters = find_common_letters_in_two_strings(string, string2)
            if common_letters:
                return common_letters
    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        strings = f.readlines()
    common_letters = find_common_letters(strings)
    print(f"Day 2, part 2: common letters are {common_letters}")
