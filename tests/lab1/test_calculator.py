import unittest

from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    """Тесты для класса Calculator."""

    def test_add(self):
        """Проверяет сложение двух чисел."""
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)

    def test_subtract(self):
        """Проверяет вычитание двух чисел."""
        calc = Calculator()
        self.assertEqual(calc.subtract(5, 3), 2)

    def test_multiply(self):
        """Проверяет умножение двух чисел."""
        calc = Calculator()
        self.assertEqual(calc.multiply(4, 3), 12)

    def test_divide(self):
        """Проверяет деление двух чисел."""
        calc = Calculator()
        self.assertEqual(calc.divide(10, 2), 5)

    # Тест для проверки работы, можно удалить
    def test_one(self):
        self.assertEqual(1, 1)

    def test_divide_by_zero(self):
        """Проверяет, что деление на ноль возбуждает ошибку."""
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.divide(5, 0)

