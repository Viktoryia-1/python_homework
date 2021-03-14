# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, p):
        self.param = p

    @abstractmethod
    def count(self):
        pass

    def __add__(self, other):
        return self.count() + other.count


class Coat(Clothes):
    @property
    def count(self):
        count_size = self.param / 6.5 + 0.5
        return round(count_size, 2)


class Suit(Clothes):
    @property
    def count(self):
        count_height = 2 * self.param + 0.3
        return round(count_height, 2)


coat = Coat(38)
suit = Suit(160)
print(coat.count)
print(suit.count)
print(round(coat.count + suit.count, 2))

