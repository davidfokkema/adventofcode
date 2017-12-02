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


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readline().rstrip()
        print(inverse_captcha(input))
