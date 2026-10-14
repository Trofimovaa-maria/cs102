import unittest

from src.lab2.rsa import gcd, generate_keypair, is_prime, multiplicative_inverse


class RSATestCase(unittest.TestCase):
    """Тесты для функций RSA."""

    """is_prime"""

    def test_is_prime_two(self):
        """2 — простое число."""
        self.assertTrue(is_prime(2))

    def test_is_prime_small_primes(self):
        """Простые числа: 3, 5, 7, 11, 13, 17, 19, 23."""
        for n in (3, 5, 7, 11, 13, 17, 19, 23):
            with self.subTest(n=n):
                self.assertTrue(is_prime(n))

    def test_is_prime_large_prime(self):
        """Большое простое число (7919)."""
        self.assertTrue(is_prime(7919))

    def test_is_prime_one(self):
        """1 — не простое число."""
        self.assertFalse(is_prime(1))

    def test_is_prime_zero(self):
        """0 — не простое число."""
        self.assertFalse(is_prime(0))

    def test_is_prime_negative(self):
        """Отрицательные числа не простые."""
        self.assertFalse(is_prime(-7))

    def test_is_prime_even_composite(self):
        """8 — составное."""
        self.assertFalse(is_prime(8))

    def test_is_prime_odd_composite(self):
        """9, 15, 21 — составные."""
        for n in (9, 15, 21, 25, 49, 100):
            with self.subTest(n=n):
                self.assertFalse(is_prime(n))

    """gcd"""

    def test_gcd_basic(self):
        """Классические примеры из doctest."""
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_gcd_coprime(self):
        """Взаимно простые числа дают 1."""
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(9, 28), 1)

    def test_gcd_same(self):
        """НОД одинаковых чисел равен самому числу."""
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(100, 100), 100)

    def test_gcd_one_is_zero(self):
        """НОД(a, 0) = a, НОД(0, b) = b."""
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 5), 5)

    def test_gcd_multiples(self):
        """НОД кратных чисел."""
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(100, 75), 25)

    """multiplicative_inverse"""

    def test_multiplicative_inverse_doc(self):
        """Пример из doctest: 7 * 23 mod 40 = 1."""
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_multiplicative_inverse_result_mod(self):
        """Проверяем свойство: (e * d) % phi == 1."""
        e, phi = 3, 40
        d = multiplicative_inverse(e, phi)
        self.assertEqual((e * d) % phi, 1)

    def test_multiplicative_inverse_various(self):
        """Проверяем свойство для нескольких пар."""
        pairs = [(3, 11), (5, 12), (7, 20), (11, 26)]
        for e, phi in pairs:
            with self.subTest(e=e, phi=phi):
                d = multiplicative_inverse(e, phi)
                self.assertEqual((e * d) % phi, 1)

    """generate_keypair"""

    def test_generate_keypair_n_equals_pq(self):
        """n = p * q."""
        p, q = 61, 53
        public, private = generate_keypair(p, q)
        e, n = public
        d, n2 = private
        self.assertEqual(n, p * q)
        self.assertEqual(n2, p * q)

    def test_generate_keypair_phi_coprime(self):
        """e и phi(n) взаимно просты, d — обратный к e по модулю phi."""
        p, q = 61, 53
        phi = (p - 1) * (q - 1)
        public, private = generate_keypair(p, q)
        e, _ = public
        d, _ = private

        self.assertEqual(gcd(e, phi), 1)
        self.assertEqual((e * d) % phi, 1)

    def test_generate_keypair_not_prime_p(self):
        """Если p не простое — ValueError."""
        with self.assertRaises(ValueError):
            generate_keypair(60, 53)

    def test_generate_keypair_not_prime_q(self):
        """Если q не простое — ValueError."""
        with self.assertRaises(ValueError):
            generate_keypair(61, 54)

    def test_generate_keypair_equal(self):
        """p == q — ValueError."""
        with self.assertRaises(ValueError):
            generate_keypair(53, 53)

    def test_generate_keypair_encrypt_decrypt(self):
        """Полный цикл: шифруем и расшифровываем число."""
        p, q = 61, 53
        public, private = generate_keypair(p, q)
        e, n = public
        d, _ = private

        message = 65  # код символа 'A'
        cipher = pow(message, e, n)
        plain = pow(cipher, d, n)
        self.assertEqual(plain, message)


if __name__ == "__main__":
    unittest.main()
