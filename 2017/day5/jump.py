def perform_jump(instructions, pointer):
    new_pointer = pointer + instructions[pointer]
    instructions[pointer] += 1
    if new_pointer >= 0 and new_pointer < len(instructions):
        return new_pointer
    else:
        return None


def perform_strange_jump(instructions, pointer):
    new_pointer = pointer + instructions[pointer]
    if instructions[pointer] >= 3:
        instructions[pointer] -= 1
    else:
        instructions[pointer] += 1
    if new_pointer >= 0 and new_pointer < len(instructions):
        return new_pointer
    else:
        return None


def number_of_jumps_to_escape(instructions, pointer, jump_func=perform_jump):
    N = 0
    while True:
        try:
            pointer = jump_func(instructions, pointer)
        except TypeError:
            break
        else:
            N += 1
    return N


def number_of_strange_jumps_to_escape(instructions, pointer):
    return number_of_jumps_to_escape(instructions, pointer,
                                     jump_func=perform_strange_jump)


if __name__ == '__main__':
    with open('input.txt') as f:
        instructions = [int(u) for u in f.readlines()]
        print("Day 5, part 1:", number_of_jumps_to_escape(
            instructions.copy(), 0))
        print("Day 5, part 2:", number_of_strange_jumps_to_escape(
            instructions.copy(), 0))
