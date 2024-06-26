import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
    
    def test_power_method_fails_with_strings(self):
        self.assertRaises(TypeError, self.calc.power, "4", "32")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, "3", "5")
        self.assertRaises(TypeError, self.calc.power, "4", "4")

    def test_power_method_returns_correct_result(self):
        self.assertEqual(25, self.calc.power(5, 2))
        self.assertEqual(3, self.calc.power(3, 1))
        self.assertEqual(1024, self.calc.power(4, 5))
        self.assertEqual(216, self.calc.power(6, 3))

    def test_squareroot_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.squareroot, -1)
        self.assertRaises(TypeError, self.calc.squareroot, "5")
        self.assertRaises(TypeError, self.calc.squareroot, -10)
        self.assertRaises(TypeError, self.calc.squareroot, -4)

    def test_squareroot_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.squareroot(25))
        self.assertEqual(2, self.calc.squareroot(4))
        self.assertEqual(8, self.calc.squareroot(64))
        self.assertEqual(9, self.calc.squareroot(81))

    def test_logarithmbaseten_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.logarithmbaseten, "-5")
        self.assertRaises(TypeError, self.calc.logarithmbaseten, -10)
        self.assertRaises(TypeError, self.calc.logarithmbaseten, -3)
        self.assertRaises(TypeError, self.calc.logarithmbaseten, -42)

    def test_logarithmbaseten_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.logarithmbaseten(1))
        self.assertEqual(1, self.calc.logarithmbaseten(10))
        self.assertEqual(2, self.calc.logarithmbaseten(100))
        self.assertEqual(3, self.calc.logarithmbaseten(1000))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
