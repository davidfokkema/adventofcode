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
    def __init__(self, ring):
        self.ring = ring

    def tie_all_knots(self, position, lengths):
        skip = 0
        for length in lengths:
            self.tie_knot(position, length)
            position += length + skip
            skip += 1

    def tie_knot(self, position, length):
        start, stop = position, position + length
        self.ring[start:stop] = self.ring[stop - 1:start - 1: -1]


if __name__ == '__main__':
    with open('input.txt') as f:
        lengths = [int(u) for u in f.readline().split(',')]

    hash = KnotHash(Ring(range(256)))
    hash.tie_all_knots(0, lengths)
    print("Day 10, part 1:", hash.ring[0] * hash.ring[1])
