import itertools
import time


def number_of_steps(square_id):
    x, y = get_coordinates_for_square(square_id)
    return manhattan_distance(x, y)


def get_coordinates_for_square(square_id):
    return list(itertools.islice(generate_grid_positions(), square_id - 1,
                                 square_id))[0]


def generate_memory_cells():
    mem_store = {}
    for x, y in generate_grid_positions():
        if x == y == 0:
            mem = 1
        else:
            mem = 0
            for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if not dx == dy == 0:
                    try:
                        mem += mem_store[(x + dx, y + dy)]
                    except KeyError:
                        pass
        mem_store[(x, y)] = mem
        yield mem


def first_memory_cell_greater_than(N):
    for mem in generate_memory_cells():
        if mem > N:
            return mem


def generate_grid_positions():
    x, y = 0, 0
    for direction in generate_spiral_steps():
        yield (x, y)
        if direction == 'RIGHT':
            x += 1
        elif direction == 'UP':
            y += 1
        elif direction == 'LEFT':
            x -= 1
        elif direction == 'DOWN':
            y -= 1


def generate_spiral_steps():
    directions = itertools.cycle(['RIGHT', 'UP', 'LEFT', 'DOWN'])
    step_increase = itertools.cycle([0, 1])

    number_of_steps = 1
    for direction in directions:
        for i in range(number_of_steps):
            yield direction
        number_of_steps += next(step_increase)


def manhattan_distance(x, y):
    return abs(x) + abs(y)


if __name__ == '__main__':
    print(number_of_steps(325489))
    print(first_memory_cell_greater_than(325489))
