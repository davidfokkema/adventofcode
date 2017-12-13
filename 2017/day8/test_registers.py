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
        code, comparison = self.registers.parse_instruction('b inc 5 if a > 1')
        self.assertEqual(code, ('b', 'inc', 5))
        self.assertEqual(comparison, ('a', '>', 1))

    def test_is_true(self):
        self.registers.registers = {'a': 10}

        self.assertTrue(self.registers.is_true(('a', '>', 1)))
        self.assertFalse(self.registers.is_true(('a', '>', 10)))

        self.assertTrue(self.registers.is_true(('foo', '>', -1)))
        self.assertFalse(self.registers.is_true(('bar', '>', 0)))

        self.assertTrue(self.registers.is_true(('a', '<', 11)))
        self.assertFalse(self.registers.is_true(('a', '<', 9)))

        self.assertTrue(self.registers.is_true(('a', '==', 10)))
        self.assertFalse(self.registers.is_true(('a', '==', 1)))

        self.assertTrue(self.registers.is_true(('a', '!=', 1)))
        self.assertFalse(self.registers.is_true(('a', '!=', 10)))

        self.assertTrue(self.registers.is_true(('a', '>=', 9)))
        self.assertTrue(self.registers.is_true(('a', '>=', 10)))
        self.assertFalse(self.registers.is_true(('a', '>=', 11)))

        self.assertTrue(self.registers.is_true(('a', '<=', 11)))
        self.assertTrue(self.registers.is_true(('a', '<=', 10)))
        self.assertFalse(self.registers.is_true(('a', '<=', 9)))

        with self.assertRaises(RuntimeError):
            self.registers.is_true(('a', '===', 1))

    def test_excecute_instruction(self):
        self.registers.registers = {}

        self.registers.execute_instruction(('a', 'inc', 1))
        self.assertEqual(self.registers.registers['a'], 1)
        self.registers.execute_instruction(('a', 'inc', 2))
        self.assertEqual(self.registers.registers['a'], 3)

        self.registers.execute_instruction(('b', 'dec', 1))
        self.assertEqual(self.registers.registers['b'], -1)
        self.registers.execute_instruction(('b', 'dec', 2))
        self.assertEqual(self.registers.registers['b'], -3)

        self.registers.execute_instruction(('b', 'inc', 10))
        self.assertEqual(self.registers.registers['b'], 7)

        with self.assertRaises(RuntimeError):
            self.registers.execute_instruction(('a', 'mul', 2))


if __name__ == '__main__':
    unittest.main()
