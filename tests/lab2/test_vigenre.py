import unittest

from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere


class VigenereTestCase(unittest.TestCase):
    """Тесты для функций шифра Виженера."""

    """encrypt_vigenere"""

    def test_encrypt_key_a(self):
        """Ключ A не меняет заглавные буквы."""
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")

    def test_encrypt_key_a_lower(self):
        """Строчная a тоже не меняет сообщение."""
        self.assertEqual(encrypt_vigenere("python", "a"), "python")

    def test_encrypt_lemon(self):
        """Классический пример ATTACKATDAWN + LEMON."""
        self.assertEqual(
            encrypt_vigenere("ATTACKATDAWN", "LEMON"),
            "LXFOPVEFRNHR",
        )

    def test_encrypt_key_d_equals_caesar(self):
        """Ключ D эквивалентен шифру Цезаря со сдвигом 3."""
        self.assertEqual(encrypt_vigenere("ABC", "D"), "DEF")

    def test_encrypt_key_d_lower(self):
        """Строчная d также эквивалентна сдвигу на 3."""
        self.assertEqual(encrypt_vigenere("abc", "d"), "def")

    def test_encrypt_long_key(self):
        """Ключ длиннее текста — берётся только нужная часть."""
        self.assertEqual(encrypt_vigenere("ABC", "DDDDD"), "DEF")

    def test_encrypt_empty(self):
        """Пустая строка остаётся пустой."""
        self.assertEqual(encrypt_vigenere("", "LEMON"), "")

    def test_encrypt_symbols(self):
        """Цифры и знаки препинания не шифруются."""
        self.assertEqual(encrypt_vigenere("123!@#", "LEMON"), "123!@#")

    def test_encrypt_mixed_case(self):
        """Регистр сохраняется, ключ работает и для строчных, и для заглавных."""
        self.assertEqual(encrypt_vigenere("Attack", "LEMON"), "Lxfopv")

    def test_encrypt_wrap_around(self):
        """Сдвиг переходит через Z -> A."""
        # X + D(3) = A, Y + D = B, Z + D = C
        self.assertEqual(encrypt_vigenere("XYZ", "D"), "ABC")

    def test_encrypt_key_shorter_than_text(self):
        """Ключ повторяется, если он короче текста."""
        # LEMON -> LEMONLEMONLE для ATTACKATDAWN
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    """decrypt_vigenere"""

    def test_decrypt_key_a(self):
        """Ключ A ничего не меняет."""
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")

    def test_decrypt_key_a_lower(self):
        """Строчная a — то же самое."""
        self.assertEqual(decrypt_vigenere("python", "a"), "python")

    def test_decrypt_lemon(self):
        """Обратный классический пример."""
        self.assertEqual(
            decrypt_vigenere("LXFOPVEFRNHR", "LEMON"),
            "ATTACKATDAWN",
        )

    def test_decrypt_empty(self):
        """Пустая строка остаётся пустой."""
        self.assertEqual(decrypt_vigenere("", "LEMON"), "")

    def test_decrypt_symbols(self):
        """Цифры и знаки препинания не расшифровываются."""
        self.assertEqual(decrypt_vigenere("123!@#", "LEMON"), "123!@#")

    def test_decrypt_mixed_case(self):
        """Регистр сохраняется при расшифровке."""
        self.assertEqual(decrypt_vigenere("Lxfopv", "LEMON"), "Attack")

    """Взаимная проверка"""

    def test_encrypt_then_decrypt(self):
        """Шифрование + расшифровка = исходный текст."""
        text = "Hello, World!"
        keyword = "KEY"
        self.assertEqual(
            decrypt_vigenere(encrypt_vigenere(text, keyword), keyword), text
        )

    def test_encrypt_then_decrypt_long(self):
        """То же с длинным текстом и ключом."""
        text = "The quick brown fox jumps over the lazy dog"
        keyword = "SECRET"
        self.assertEqual(
            decrypt_vigenere(encrypt_vigenere(text, keyword), keyword), text
        )

    def test_encrypt_then_decrypt_with_punctuation(self):
        """Смешанный текст с пробелами, цифрами и знаками."""
        text = "Attack at dawn! 42 times."
        keyword = "LEMON"
        self.assertEqual(
            decrypt_vigenere(encrypt_vigenere(text, keyword), keyword), text
        )


if __name__ == "__main__":
    unittest.main()
