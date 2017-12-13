import unittest
from unittest.mock import patch

from registers import Registers


class RegisterTest(unittest.TestCase):
    def setUp(self):
        self.registers = Registers()

    @patch.object(Registers, 'parse_instruction')
    @patch.object(Registers, 'is_true')
    @patch.object(Registers, 'execute_instruction')
    def test_process_and_execute_instruction(self, mock_execute, mock_is_true,
                                             mock_parse):
        mock_parse.return_value = 'b', 'inc', 5, 'a', '>', 1

        self.registers.process_and_execute_instruction('b inc 5 if a > 1')
        
        mock_parse.assert_called_once_with('b inc 5 if a > 1')
        mock_is_true.assert_called_once_with('a', '>', 1)

    def test_parse_instruction(self):
        return_values = self.registers.parse_instruction('b inc 5 if a > 1')
        self.assertEqual(return_values, ('b', 'inc', 5, 'a', '>', 1))


if __name__ == '__main__':
    unittest.main()
