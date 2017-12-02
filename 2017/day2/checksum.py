import csv


def checksum(filename):
    sum = 0
    with open(filename) as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            numbers = [int(u) for u in line]
            sum += max(numbers) - min(numbers)
    return sum


if __name__ == '__main__':
    print("Part 1:", checksum('input'))
