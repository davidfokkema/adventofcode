class FrequencyShifter(object):

    def __init__(self, frequency):
        self.frequency = frequency
        self.frequencies = []

    def calculate_frequency(self, frequency_shifts):
        frequency = self.frequency
        for shift in frequency_shifts:
            frequency += shift
        return frequency

    def find_first_duplicate_frequency(self, frequency_shifts):
        pass

    def has_duplicates(self):
        return len(self.frequencies) != len(set(self.frequencies))


def read_shifts_from_file(filename):
    with open(filename) as f:
        shifts = [int(u) for u in f.readlines()]
    return shifts


if __name__ == '__main__':
    shifter = FrequencyShifter(0)
    shifts = read_shifts_from_file('./input.txt')
    frequency = shifter.calculate_frequency(shifts)
    print(f"Day 1: frequency is {frequency}")
