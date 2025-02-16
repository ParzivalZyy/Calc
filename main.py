def add(a, b):
    """
    Сложение двух чисел.
    :param a: Первое число.
    :param b: Второе число.
    :return: Результат сложения.
    """
    return a + b


def subtract(a, b):
    """
    Вычитание двух чисел.
    :param a: Первое число.
    :param b: Второе число.
    :return: Результат вычитания.
    """
    return a - b


def multiply(a, b):
    """
    Умножение двух чисел.
    :param a: Первое число.
    :param b: Второе число.
    :return: Результат умножения.
    """
    return a * b


def divide(a, b):
    """
    Деление двух чисел.
    :param a: Первое число.
    :param b: Второе число.
    :return: Результат деления.
    :raises ValueError: Если второе число равно 0.
    """
    if b == 0:
        raise ValueError("Ошибка: деление на ноль невозможно!")
    return a / b


def main():
    """
    Основная функция для взаимодействия с пользователем.
    """
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /")

    try:
        # Ввод данных от пользователя
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        # Выполнение операции
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Ошибка: неверный оператор!")
            return

        if result % 1 == 0 :
            print(f"Результат: {int(result)}")
        else:
            print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()