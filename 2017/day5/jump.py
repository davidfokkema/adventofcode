def perform_jump(instructions, pointer):
    new_pointer = pointer + instructions[pointer]
    instructions[pointer] += 1
    if new_pointer >= 0 and new_pointer < len(instructions):
        return new_pointer
    else:
        return None
