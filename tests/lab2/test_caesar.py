import unittest

from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CaesarTestCase(unittest.TestCase):
    """Тесты для функций шифра Цезаря."""

    """encrypt_caesar"""

    def test_encrypt_upper(self):
        """Зашифровывает заглавные буквы."""
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")

    def test_encrypt_lower(self):
        """Зашифровывает строчные буквы."""
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")

    def test_encrypt_mixed(self):
        """Не трогает цифры и знаки препинания."""
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")

    def test_encrypt_empty(self):
        """Пустая строка остаётся пустой."""
        self.assertEqual(encrypt_caesar(""), "")

    def test_encrypt_shift_zero(self):
        """Сдвиг 0 не меняет текст."""
        self.assertEqual(encrypt_caesar("ABC", 0), "ABC")

    def test_encrypt_shift_custom(self):
        """Произвольный сдвиг (например, 1)."""
        self.assertEqual(encrypt_caesar("ABC", 1), "BCD")

    def test_encrypt_wrap_around(self):
        """Сдвиг переходит через Z -> A."""
        self.assertEqual(encrypt_caesar("XYZ"), "ABC")

    def test_encrypt_wrap_around_lower(self):
        """Сдвиг переходит через z -> a."""
        self.assertEqual(encrypt_caesar("xyz"), "abc")

    def test_encrypt_only_symbols(self):
        """Строка без букв не изменяется."""
        self.assertEqual(encrypt_caesar("123!@#"), "123!@#")

    '''decrypt_caesar'''

    def test_decrypt_upper(self):
        """Расшифровывает заглавные буквы."""
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")

    def test_decrypt_lower(self):
        """Расшифровывает строчные буквы."""
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")

    def test_decrypt_mixed(self):
        """Не трогает цифры и знаки препинания."""
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")

    def test_decrypt_empty(self):
        """Пустая строка остаётся пустой."""
        self.assertEqual(decrypt_caesar(""), "")

    def test_decrypt_shift_zero(self):
        """Сдвиг 0 не меняет текст."""
        self.assertEqual(decrypt_caesar("ABC", 0), "ABC")

    def test_decrypt_wrap_around(self):
        """Обратный переход через A -> Z."""
        self.assertEqual(decrypt_caesar("ABC"), "XYZ")

    # ---------- Взаимная проверка ----------

    def test_encrypt_then_decrypt(self):
        """Шифрование и расшифровка возвращают исходный текст."""
        text = "Hello, World!"
        self.assertEqual(decrypt_caesar(encrypt_caesar(text)), text)

    def test_encrypt_then_decrypt_custom_shift(self):
        """То же самое с произвольным сдвигом."""
        text = "Python 3.13"
        self.assertEqual(decrypt_caesar(encrypt_caesar(text, 7), 7), text)


if __name__ == "__main__":
    unittest.main()