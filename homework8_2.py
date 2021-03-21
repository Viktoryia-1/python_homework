# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.
class MyError(Exception):
    def __init__(self, n, d):

        self.numerator = n
        self.denominator = d

    def my_zero_error(self):
        try:
            return self.numerator / self.denominator
        except:
            if self.denominator == 0:
                return f"You can not divide on zero"


a = MyError(10, 0)
print(a.my_zero_error())
















