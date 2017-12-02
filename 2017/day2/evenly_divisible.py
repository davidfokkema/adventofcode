import csv
import itertools


def find_evenly_divisible_numbers(numbers):
    for a, b in itertools.permutations(numbers, 2):
        if not (a % b):
            return a, b


def divide_evenly_divisible_numbers(numbers):
    a, b = find_evenly_divisible_numbers(numbers)
    return a // b


def calculate_checksum(filename):
    sum = 0
    with open(filename) as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            numbers = [int(u) for u in line]
            sum += divide_evenly_divisible_numbers(numbers)
    return sum


if __name__ == '__main__':
    print("Part 2:", calculate_checksum('input'))
