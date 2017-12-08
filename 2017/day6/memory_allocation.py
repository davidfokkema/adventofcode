import numpy as np


def cycles_before_loop(memory_bank):
    num_cycles, loop_idx = perform_cycles_and_return_loop_idx(memory_bank)
    return num_cycles


def perform_cycles_and_return_loop_idx(memory_bank):
    previous_states = [memory_bank]
    num_cycles = 0
    while True:
        memory_bank = cycle(memory_bank)
        num_cycles += 1
        if memory_bank in previous_states:
            return num_cycles, previous_states.index(memory_bank)
        else:
            previous_states.append(memory_bank)


def loop_size(memory_bank):
    num_cycles, loop_idx = perform_cycles_and_return_loop_idx(memory_bank)
    loop_size = num_cycles - loop_idx
    return num_cycles, loop_size


def cycle(memory_banks):
    N = len(memory_banks)
    memory_banks = np.array(memory_banks)
    # find largest memory bank
    idx = memory_banks.argmax()
    # empty memory bank in container
    container = memory_banks[idx]
    memory_banks[idx] = 0

    # redistribute
    while container:
        idx += 1
        memory_banks[idx % N] += 1
        container -= 1

    return list(memory_banks)


if __name__ == '__main__':
    with open('input.txt') as f:
        line = f.readline()
    memory_bank = [int(u) for u in line.split('\t')]
    num_cycles, loop_size = loop_size(memory_bank)
    print("Day 6, part 1:", num_cycles)
    print("Day 6, part 2:", loop_size)
