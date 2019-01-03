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


def add_up_repose_records(records):
    added_records = defaultdict(lambda: np.zeros(60))

    for record in records:
        if 'begins shift' in record:
            guard = re.search('#\d+', record).group(0)
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
