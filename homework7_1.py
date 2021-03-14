# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, l):
        self.list = l

    def __str__(self):
        return str("\n".join([" ".join([str(i) for i in el]) for el in self.list]))

    def __add__(self, other):
        for el in range(len(self.list)):
            for i in range(len(self.list[el])):
                self.list[el][i] = self.list[el][i] + other.list[el][i]
        return str("\n".join([" ".join([str(i) for i in el]) for el in self.list]))


first_matrix = Matrix([[1, 2], [1, 2], [1, 2]])
second_matrix = Matrix([[1, 2], [1, 2], [1, 2]])
print(first_matrix.__str__())
print(type(first_matrix.__str__()))
z = first_matrix + second_matrix
print(z)
print(type(z))



