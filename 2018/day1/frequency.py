import itertools


def calculate_frequency(frequency_shifts):
    frequency = 0
    for shift in frequency_shifts:
        frequency += shift
    return frequency


def find_first_duplicate_frequency(frequency_shifts):
    frequency = 0
    frequencies = [frequency]
    for shift in itertools.cycle(frequency_shifts):
        frequency += shift
        if frequency in frequencies:
            return frequency
        else:
            frequencies.append(frequency)


def read_shifts_from_file(filename):
    with open(filename) as f:
        shifts = [int(u) for u in f.readlines()]
    return shifts


if __name__ == '__main__':
    shifts = read_shifts_from_file('./input.txt')
    frequency = calculate_frequency(shifts)
    print(f"Day 1: frequency is {frequency}")
    first_duplicate = find_first_duplicate_frequency(shifts)
    print(f"Day 1 (part 2): first duplicate frequency is {first_duplicate}")
