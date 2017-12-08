import numpy as np


def cycles_before_loop(memory_bank):
    previous_states = [memory_bank]
    num_cycles = 0
    while True:
        memory_bank = cycle(memory_bank)
        num_cycles += 1
        if memory_bank in previous_states:
            return num_cycles
        else:
            previous_states.append(memory_bank)


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
