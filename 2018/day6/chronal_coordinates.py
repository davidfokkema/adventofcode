import numpy as np


def find_largest_area(coordinates):
    size_x, size_y = np.array(coordinates).max(axis=0) + 2
    grid = np.zeros(shape=(size_x, size_y), dtype=int)

    for x in range(size_x):
        for y in range(size_y):
            grid[x, y] = find_closest_coordinate((x, y), coordinates)

    for y in range(size_y):
        for x in range(size_x):
            print(get_letter(grid[x, y]), end='')
        print()


def calculate_manhattan_distances(position, coordinates):
    X, Y = position
    xs, ys = np.array(coordinates).T
    return abs(X - xs) + abs(Y - ys)


def find_closest_coordinate(position, coordinates):
    if position in coordinates:
        return -(coordinates.index(position) + 1)
    else:
        distances = calculate_manhattan_distances(position, coordinates)
        min_distance = min(distances)
        num_closest = (distances == min_distance).sum()
        # print(f"{position}: {min_distance}, {num_closest}, {distances}")
        if num_closest == 1:
            return distances.argmin() + 1
        else:
            return 0


def get_letter(code):
    if code > 0:
        return chr(ord('a') + code - 1)
    elif code < 0:
        return chr(ord('A') - code - 1)
    else:
        return '.'
