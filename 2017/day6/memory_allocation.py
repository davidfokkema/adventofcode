import numpy as np

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
