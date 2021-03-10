# Реализовать класс Road(дорога).
# определить атрибуты: length(длина), width(ширина);
# значения атрибутов должны передаваться при
# создании экземпляра класса; атрибуты сделать
# защищёнными; определить метод расчёта массы асфальта, необходимого
# для покрытия всей дороги; использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв.метра дороги асфальтом, толщиной
# в 1 см * число см толщины полотна; проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500т.

class Road:

    def count_weight(self, _length, _width, cent_mass, cent_count):
        weight = (_length * _width * cent_mass * cent_count) / 1000
        return weight


a = Road()
a = a.count_weight(20, 5000, 25, 5)
print(a)