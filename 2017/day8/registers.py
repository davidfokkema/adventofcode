class Registers(object):
    def __init__(self):
        self.registers = {}

    def parse_file(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                self.process_and_execute_instruction(line)

    def process_and_execute_instruction(self, instruction):
        code, comparison = self.parse_instruction(instruction)
        if self.is_true(comparison):
            self.execute_instruction(code)

    def parse_instruction(self, instruction):
        register, operator, value, _, rel_register, rel_operator, rel_value = \
            instruction.split()

        value = int(value)
        rel_value = int(rel_value)

        return (register, operator, value), (rel_register, rel_operator,
                                             rel_value)

    def is_true(self, comparison):
        register, operator, value = comparison
        reg_value = self.registers.get(register, 0)
        if operator == '>':
            return reg_value > value
        elif operator == '<':
            return reg_value < value
        elif operator == '==':
            return reg_value == value
        elif operator == '!=':
            return reg_value != value
        elif operator == '>=':
            return reg_value >= value
        elif operator == '<=':
            return reg_value <= value
        raise RuntimeError("Unknown operator", operator)

    def execute_instruction(self, code):
        register, operator, value = code
        self.registers.setdefault(register, 0)
        if operator == 'inc':
            self.registers[register] += value
        elif operator == 'dec':
            self.registers[register] -= value
        else:
            raise RuntimeError("Unknown operator", operator)

    def get_largest_value(self):
        return max(self.registers.values())


if __name__ == '__main__':
    registers = Registers()
    registers.parse_file('input.txt')
    print("Day 8, part 1:", registers.get_largest_value())
