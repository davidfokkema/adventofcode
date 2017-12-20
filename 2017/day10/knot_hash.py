class Ring(object):

    """Circular list"""

    def __init__(self, values):
        self._ring = list(values)
        self._len = len(self._ring)

    def __getitem__(self, index):
        if type(index) == int:
            return self._ring[index % self._len]
        elif type(index) == slice:
            start, stop, step = index.start, index.stop, index.step
            if step is None:
                step = 1
            return [self.__getitem__(idx) for idx in range(start, stop, step)]

    def __setitem__(self, index, value):
        if type(index) == int:
            self._ring[index % self._len] = value
        elif type(index) == slice:
            value_list = value
            start, stop, step = index.start, index.stop, index.step
            if step is None:
                step = 1
            for idx, value in zip(range(start, stop, step), value_list):
                self.__setitem__(idx, value)


class KnotHash(object):
    position = 0
    skip = 0

    def __init__(self):
        self.ring = Ring(range(256))

    def calculate_hash(self, input):
        lengths = self.get_lengths_from_string(input)
        for i in range(64):
            self.tie_all_knots(lengths)
        dense_hash = self.reduce_sparse_hash()

        return ''.join(['{:02x}'.format(u) for u in dense_hash])

    def get_lengths_from_string(self, input):
        return [ord(u) for u in input] + [17, 31, 73, 47, 23]

    def reduce_sparse_hash(self):
        hash_values = []
        for i in range(0, 256, 16):
            value = self.ring[i]
            for u in self.ring[i + 1:i + 16]:
                value ^= u
            hash_values.append(value)
        return hash_values

    def tie_all_knots(self, lengths):
        for length in lengths:
            self.tie_knot(self.position, length)
            self.position += length + self.skip
            self.skip += 1

    def tie_knot(self, position, length):
        start, stop = position, position + length
        self.ring[start:stop] = self.ring[stop - 1:start - 1: -1]


if __name__ == '__main__':
    with open('input.txt') as f:
        lengths = [int(u) for u in f.readline().split(',')]
    hash = KnotHash()
    hash.tie_all_knots(lengths)
    print("Day 10, part 1:", hash.ring[0] * hash.ring[1])

    with open('input.txt') as f:
        input = f.readline().strip()
    hash = KnotHash()
    print("Day 10, part 2:", hash.calculate_hash(input))
