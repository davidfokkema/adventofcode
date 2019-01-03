import re

import numpy as np


claim_regexp = '#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'


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
            if self.is_claim_intact(claim):
                id, _, _, _, _ = self.get_claim_properties(claim)
                return id
        return None

    def process_claim(self, claim):
        _, x, y, width, height = self.get_claim_properties(claim)
        self.fabric[x:x + width, y:y + height] += 1

    def is_claim_intact(self, claim):
        _, x, y, width, height = self.get_claim_properties(claim)
        return (self.fabric[x:x + width, y:y + height] == 1).all()

    @classmethod
    def calculate_claim_size(cls, claim):
        _, x, y, width, height = cls.get_claim_properties(claim)
        return (x + width, y + height)

    @classmethod
    def calculate_fabric_size(cls, claims):
        sizes_x, sizes_y = [], []
        for claim in claims:
            size_x, size_y = cls.calculate_claim_size(claim)
            sizes_x.append(size_x)
            sizes_y.append(size_y)
        return (max(sizes_x), max(sizes_y))

    @staticmethod
    def get_claim_properties(claim):
        match = re.match(claim_regexp, claim)
        return [int(u) for u in match.groups()]


if __name__ == '__main__':
    with open('input.txt') as f:
        claims = f.readlines()

    fabric = Fabric(claims)
    fabric.process_claims()
    num_squares = fabric.count_overlapping_squares()
    print(f"Day 3, part 1: number of overlapping squares is {num_squares}")

    claim_id = fabric.find_intact_claim_id()
    print(f"Day 3, part 2: intact claim id is {claim_id}")
