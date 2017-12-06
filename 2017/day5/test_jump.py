import re
import unittest

import jump


JUMP_SEQUENCE = ['(0) 3  0  1  -3 ',
                 '(1) 3  0  1  -3 ',
                 ' 2 (3) 0  1  -3 ',
                 ' 2  4  0  1 (-3)',
                 ' 2 (4) 0  1  -2 ',
                 ' 2  5  0  1  -2 ']


def analyze_jump_sequence(sequence):
    jump_sequence = []
    for step in sequence:
        pointer, instructions = analyze_jump_step(step)
        jump_sequence.append((pointer, instructions))
    return jump_sequence


def analyze_jump_step(step):
    instructions = re.findall('[-(0-9)]+', step)
    pointer = None
    cleaned_instructions = []
    for idx, instruction in enumerate(instructions):
        if instruction[0] == '(' and instruction[-1] == ')':
            instruction = instruction.strip('()')
            pointer = idx
        cleaned_instructions.append(int(instruction))
    return pointer, cleaned_instructions


class JumpTest(unittest.TestCase):
    def test_perform_jump(self):
        jump_sequence = analyze_jump_sequence(JUMP_SEQUENCE)

        actual_pointer, actual_instructions = jump_sequence[0]
        for expected_pointer, expected_instructions in jump_sequence:
            print("Check", expected_pointer, expected_instructions)
            self.assertEqual(expected_pointer, actual_pointer)
            self.assertEqual(expected_instructions, actual_instructions)
            if actual_pointer is not None:
                actual_pointer = jump.perform_jump(actual_instructions,
                                                   actual_pointer)


if __name__ == '__main__':
    unittest.main()
