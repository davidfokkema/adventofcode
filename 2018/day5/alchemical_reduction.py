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


if __name__ == '__main__':
    with open('input.txt') as f:
        polymer = f.read().rstrip()
    reduced_polymer = reduce_polymer(polymer)

    reduced_reduced_polymer = reduce_polymer(reduced_polymer)
    assert reduced_reduced_polymer == reduced_polymer

    print(f"Day 5, part 1: {len(reduced_polymer)} units remaining.")
