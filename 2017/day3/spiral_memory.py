import itertools
import time


def number_of_steps(square_id):
    x, y = get_coordinates_for_square(square_id)
    return manhattan_distance(x, y)


def get_coordinates_for_square(square_id):
    x, y = 0, 0
    for direction in itertools.islice(generate_spiral_steps(), 0,
                                      square_id - 1):
        if direction == 'RIGHT':
            x += 1
        elif direction == 'UP':
            y += 1
        elif direction == 'LEFT':
            x -= 1
        elif direction == 'DOWN':
            y -= 1
    return (x, y)


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
    for step in generate_spiral_steps():
        print(step)
        time.sleep(.5)
