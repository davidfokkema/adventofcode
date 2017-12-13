import unittest
from unittest.mock import patch, sentinel

from registers import Registers


class ProcessAndExecuteTest(unittest.TestCase):
    def setUp(self):
        patcher1 = patch.object(Registers, 'parse_instruction')
        self.mock_parse = patcher1.start()
        patcher2 = patch.object(Registers, 'is_true')
        self.mock_is_true = patcher2.start()
        patcher3 = patch.object(Registers, 'execute_instruction')
        self.mock_execute = patcher3.start()

        self.registers = Registers()

        self.mock_parse.return_value = sentinel.code, sentinel.comparison

        self.addCleanup(patcher1.stop)
        self.addCleanup(patcher2.stop)
        self.addCleanup(patcher3.stop)

    def test_calls_parse_with_instruction(self):
        self.registers.process_and_execute_instruction(sentinel.instruction)
        self.mock_parse.assert_called_once_with(sentinel.instruction)

    def test_calls_is_true_with_comparison(self):
        self.registers.process_and_execute_instruction('instruction')
        self.mock_is_true.assert_called_once_with(sentinel.comparison)

    def test_calls_perform_instruction_only_if_is_true(self):
        self.mock_is_true.return_value = True
        self.registers.process_and_execute_instruction('instruction')
        self.mock_execute.assert_called_once_with(sentinel.code)

        self.mock_execute.reset_mock()

        self.mock_is_true.return_value = False
        self.registers.process_and_execute_instruction('instruction')
        self.assertFalse(self.mock_execute.called)


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.registers = Registers()

    def test_parse_instruction(self):
        return_values = self.registers.parse_instruction('b inc 5 if a > 1')
        self.assertEqual(return_values, ('b', 'inc', 5, 'a', '>', 1))


if __name__ == '__main__':
    unittest.main()
