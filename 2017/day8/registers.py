class Registers(object):
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
