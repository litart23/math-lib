def add(a, b):
    """
    Складывает два числа.

    :param a: Первое число.
    :param b: Второе число.
    :return: Сумма a и b.
    """
    return a + b

def subtract(a, b):
    """
    Вычитает второе число из первого.

    :param a: Первое число.
    :param b: Второе число.
    :return: Разность a и b.
    """
    return a - b

def multiply(a, b):
    """
    Умножает два числа.

    :param a: Первое число.
    :param b: Второе число.
    :return: Произведение a и b.
    """
    return a * b

def divide(a, b):
    """
    Делит первое число на второе.

    :param a: Первое число.
    :param b: Второе число.
    :return: Результат деления a на b.
    :raises ZeroDivisionError: Если b равно 0.
    """
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль!")
    return a / b