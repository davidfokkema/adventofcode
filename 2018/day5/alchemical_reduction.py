def reduce_polymer(polymer):
    polymer = list(polymer)
    idx = 0
    while True:
        try:
            first, second = polymer[idx:idx + 2]
        except ValueError:
            break
        if first.lower() == second.lower():
            if first != second:
                del polymer[idx:idx + 2]
                if idx > 0:
                    idx -= 1
                continue
        idx += 1
    return ''.join(polymer)


def remove_type_and_react(polymer, type):
    polymer = polymer.replace(type.lower(), '')
    polymer = polymer.replace(type.upper(), '')
    return reduce_polymer(polymer)


def find_length_of_shortest_polymer(polymer):
    lengths = []
    for i in range(ord('a'), ord('z') + 1):
        reacted_polymer = remove_type_and_react(polymer, chr(i))
        lengths.append(len(reacted_polymer))
    return min(lengths)


if __name__ == '__main__':
    with open('input.txt') as f:
        polymer = f.read().rstrip()
    reduced_polymer = reduce_polymer(polymer)

    reduced_reduced_polymer = reduce_polymer(reduced_polymer)
    assert reduced_reduced_polymer == reduced_polymer

    print(f"Day 5, part 1: {len(reduced_polymer)} units remaining.")

    min_length = find_length_of_shortest_polymer(polymer)
    print(f"Day 5, part 2: {min_length} units remaining.")
