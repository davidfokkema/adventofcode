def inverse_captcha(input):
    next_digits = input[1:] + input[0]
    sum = 0

    for digit, next_digit in zip(input, next_digits):
        if digit == next_digit:
            sum += int(digit)

    return sum


def oneline_inverse_captcha(input):
    # This is hardly any faster!
    return sum([int(u) for u, v in zip(input, input[1:] + input[0]) if u == v])


def halfway_inverse_captcha(input):
    halfway = len(input) // 2
    next_halfway_digits = input[halfway:] + input[:halfway]
    sum = 0

    for digit, next_halfway_digit in zip(input, next_halfway_digits):
        if digit == next_halfway_digit:
            sum += int(digit)

    return sum



if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readline().rstrip()
        print("Part 1:", inverse_captcha(input))
        print("Part 2:", halfway_inverse_captcha(input))
