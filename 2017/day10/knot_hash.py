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
