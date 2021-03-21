# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class ZeroError(Exception):
    def __init__(self, t):
        self.text = t


try:
    numerator = int(input("Введите числитель"))
    denominator = int(input("Введите знаменатель"))
    if denominator == 0:
        raise ZeroError("Деление на ноль невозможно")
except ZeroError as error:
    print(error)
except ValueError as error:
    print("Это не число")
else:
    result = numerator / denominator
    print(result)
finally:
    print("Рассчет закончен")