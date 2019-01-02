from collections import namedtuple
import re

import numpy as np


claim_regexp = '#(?P<claim_id>\d+) @ (?P<x>\d+),(?P<y>\d+): ' \
               '(?P<width>\d+)x(?P<height>\d+)'


class Fabric(object):

    def __init__(self, claims):
        self.claims = claims
        size_x, size_y = self.calculate_fabric_size(claims)
        self.fabric = np.zeros((size_x, size_y))

    def process_claims(self):
        for claim in self.claims:
            self.process_claim(claim)

    def count_overlapping_squares(self):
        return (self.fabric >= 2).sum()

    def find_intact_claim_id(self):
        for claim in self.claims:
            if self.check_intact_claim(claim):
                return self.get_claim_id(claim)
        return None

    def process_claim(self, claim):
        match = re.match(claim_regexp, claim)
        x, y, width, height = [int(match.group(u)) for u in ['x', 'y', 'width',
                                                             'height']]
        self.fabric[x:x + width, y:y + height] += 1

    def check_intact_claim(self, claim):
        match = re.match(claim_regexp, claim)
        x, y, width, height = [int(match.group(u)) for u in ['x', 'y', 'width',
                                                             'height']]
        return (self.fabric[x:x + width, y:y+ height] == 1).all()

    @staticmethod
    def calculate_claim_size(claim):
        match = re.match(claim_regexp, claim)
        size_x = int(match.group('x')) + int(match.group('width'))
        size_y = int(match.group('y')) + int(match.group('height'))
        return (size_x, size_y)

    @classmethod
    def calculate_fabric_size(cls, claims):
        sizes_x, sizes_y = [], []
        for claim in claims:
            size_x, size_y = cls.calculate_claim_size(claim)
            sizes_x.append(size_x)
            sizes_y.append(size_y)
        return (max(sizes_x), max(sizes_y))

    def get_claim_id(self, claim):
        match = re.match(claim_regexp, claim)
        return int(match.group('claim_id'))


if __name__ == '__main__':
    with open('input.txt') as f:
        claims = f.readlines()

    fabric = Fabric(claims)
    fabric.process_claims()
    num_squares = fabric.count_overlapping_squares()
    print(f"Day 3, part 1: number of overlapping squares is {num_squares}")

    claim_id = fabric.find_intact_claim_id()
    print(f"Day 3, part 2: intact claim id is {claim_id}")
