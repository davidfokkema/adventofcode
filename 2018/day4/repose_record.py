from collections import defaultdict
import re

import numpy as np


def find_guard_with_most_sleep(records):
    totals = [v.sum() for v in records.values()]
    idx = totals.index(max(totals))
    return list(records.keys())[idx]


def find_minute_with_most_sleep(records, guard):
    minutes = records[guard]
    return minutes.argmax()


def find_most_slept_minute_overall(records):
    max_sleep_counts = [v.max() for v in records.values()]
    idx = max_sleep_counts.index(max(max_sleep_counts))
    guard = list(records.keys())[idx]
    minute = records[guard].argmax()
    return minute, guard


def add_up_repose_records(records):
    added_records = defaultdict(lambda: np.zeros(60))

    for record in records:
        if 'begins shift' in record:
            guard = int(re.search('#(\d+)', record).group(1))
        else:
            minute = int(re.search(':(\d+)', record).group(1))
            if 'falls asleep' in record:
                start = minute
            elif 'wakes up' in record:
                end = minute
                added_records[guard][start:end] += 1
            else:
                raise RuntimeError("Unknown record")

    return added_records


if __name__ == '__main__':
    with open('input.txt') as f:
        records = sorted(f.readlines())

    records = add_up_repose_records(records)

    guard = find_guard_with_most_sleep(records)
    minute = find_minute_with_most_sleep(records, guard)
    print(f"Day 4, part 1: {guard * minute}")

    minute, guard = find_most_slept_minute_overall(records)
    print(f"Day 4, part 2: {guard * minute}")
