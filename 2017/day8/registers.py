class Registers(object):
    def process_and_execute_instruction(self, instruction):
        register, operator, value, rel_register, rel_operator, rel_value = \
            self.parse_instruction(instruction)
        self.is_true(rel_register, rel_operator, rel_value)

    def parse_instruction(self, instruction):
        register, operator, value, _, rel_register, rel_operator, rel_value = \
            instruction.split()

        value = int(value)
        rel_value = int(rel_value)

        return register, operator, value, rel_register, rel_operator, rel_value

    def is_true(self):
        raise RuntimeError()

    def execute_instruction(self):
        pass
