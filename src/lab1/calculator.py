class Calculator:
    """Математические операции."""

    def add(self, a: float, b: float) -> float:
        """Возвращает сумму двух чисел."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Возвращает частное двух чисел."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение двух чисел."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Возвращает деление двух чисел."""
        return a / b

    def power(self, a: float, b: float) -> float:
        """Возвращает основание, возведённое в степень."""
        return a**b
