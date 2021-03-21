# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class NumComplex:
    def __init__(self, a, b):
        self.real = a
        self.unreal = b
        self.all = a + b

    def __add__(self, other):
        return self.real + other.real + self.unreal + other.unreal

    def __mul__(self, other):
        return self.all * other.all


a = NumComplex(1, 2j)
b = NumComplex(1, 2j)
print(a + b)
print(a * b)