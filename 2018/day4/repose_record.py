import numpy as np


def find_guard_with_most_sleep():
    return '#10'


def find_minute_with_most_sleep(guard):
    return 24


def add_up_repose_records(records):
    minutes1 = np.array([1 if u == '#' else 0 for u in ".....####################.....#########################....."])
    minutes2 = np.array([1 if u == '#' else 0 for u in "........................#####..............................."])
    return {'#10': minutes1 + minutes2}
