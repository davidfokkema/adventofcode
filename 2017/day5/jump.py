def perform_jump(instructions, pointer):
    new_pointer = pointer + instructions[pointer]
    instructions[pointer] += 1
    if new_pointer >= 0 and new_pointer < len(instructions):
        return new_pointer
    else:
        return None


def number_of_jumps_to_escape(instructions, pointer):
    N = 0
    while True:
        try:
            pointer = perform_jump(instructions, pointer)
        except TypeError:
            break
        else:
            N += 1
    return N


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [int(u) for u in f.readlines()]
        print("Day 5, part 1:", number_of_jumps_to_escape(instructions, 0))
