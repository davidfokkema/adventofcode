import re


claim_regexp = '#(?P<claim_id>\d+) @ (?P<x>\d+),(?P<y>\d+): ' \
               '(?P<width>\d+)x(?P<height>\d+)'


def calculate_claim_size(claim):
    match = re.match(claim_regexp, claim)
    size_x = int(match.group('x')) + int(match.group('width'))
    size_y = int(match.group('y')) + int(match.group('height'))
    return (size_x, size_y)


def calculate_fabric_size(claims):
    sizes_x, sizes_y = [], []
    for claim in claims:
        size_x, size_y = calculate_claim_size(claim)
        sizes_x.append(size_x)
        sizes_y.append(size_y)
    return (max(sizes_x), max(sizes_y))
