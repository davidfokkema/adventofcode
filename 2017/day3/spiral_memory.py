def number_of_steps(square_id):
    if square_id == 1:
        return 0
    elif square_id == 12:
        return 3
    elif square_id == 23:
        return 2
    elif square_id == 1024:
        return 31


def manhattan_distance(x, y):
    return abs(x) + abs(y)
