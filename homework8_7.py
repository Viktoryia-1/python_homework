# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumbers:
    def __init__(self, num_1):
        self.num_1 = num_1

    def __add__(self, other):
        return self.num_1 + other

    def __mul__(self, other):
        return self.num_1 * other


a = ComplexNumbers(1 + 2j)
a = a.num_1
b = ComplexNumbers(1 + 2j)
b = b.num_1
print(a + b)
print(a * b)

