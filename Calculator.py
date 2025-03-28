"""
Модуль calculator.py

Этот модуль предоставляет базовые арифметические операции и демонстрирует 
документирование кода для Sphinx.
"""

def add(a: float, b: float) -> float:
    """
    Складывает два числа и возвращает результат.

    :param a: Первое слагаемое
    :type a: float
    :param b: Второе слагаемое
    :type b: float
    :return: Сумма a и b
    :rtype: float

    Пример использования:
        >>> add(2, 3)
        5.0
    """
    return float(a + b)


def subtract(a: float, b: float) -> float:
    """
    Вычитает второе число из первого и возвращает результат.

    :param a: Уменьшаемое
    :type a: float
    :param b: Вычитаемое
    :type b: float
    :return: Разность a и b
    :rtype: float

    Пример использования:
        >>> subtract(5, 3)
        2.0
    """
    return float(a - b)


def multiply(a: float, b: float) -> float:
    """
    Умножает два числа и возвращает результат.

    :param a: Первый множитель
    :type a: float
    :param b: Второй множитель
    :type b: float
    :return: Произведение a и b
    :rtype: float

    Пример использования:
        >>> multiply(2, 3)
        6.0
    """
    return float(a * b)


def divide(a: float, b: float) -> float:
    """
    Делит первое число на второе и возвращает результат.

    :param a: Делимое
    :type a: float
    :param b: Делитель (не должен быть нулем)
    :type b: float
    :return: Частное a и b
    :rtype: float
    :raises ValueError: Если b равно нулю

    Пример использования:
        >>> divide(6, 3)
        2.0
    """
    if b == 0:
        raise ValueError("Делитель не может быть нулем")
    return float(a / b)


class Calculator:
    """
    Класс Calculator предоставляет методы для выполнения арифметических операций 
    с сохранением истории вычислений.

    :ivar history: Список для хранения истории операций
    :vartype history: list[str]
    """

    def __init__(self):
        """Инициализирует новый калькулятор с пустой историей операций."""
        self.history = []

    def add(self, a: float, b: float) -> float:
        """
        Складывает два числа, сохраняет операцию в истории и возвращает результат.

        :param a: Первое слагаемое
        :type a: float
        :param b: Второе слагаемое
        :type b: float
        :return: Сумма a и b
        :rtype: float
        """
        result = add(a, b)
        self.history.append(f"{a} + {b} = {result}")
        return result

    def get_history(self) -> list[str]:
        """
        Возвращает историю операций калькулятора.

        :return: Список выполненных операций
        :rtype: list[str]
        """
        return self.history


if __name__ == "__main__":
    # Пример использования модуля
    print("2 + 3 =", add(2, 3))
    print("5 - 3 =", subtract(5, 3))
    
    calc = Calculator()
    print("10 * 2 =", calc.add(10, 2))
    print("История операций:", calc.get_history())