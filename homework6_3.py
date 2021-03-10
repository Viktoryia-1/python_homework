# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name = "Helen"
    surname = "Malajowa"
    position = "Manager"
    _income = {"wage": 10000, "bonus": 0.5}


class Position(Worker):

    def get_full_name(self, name, surname):
        print(name, surname)

    def get_total_income(self, _income):
        total_income = int(_income.get("wage") + _income.get("wage") * _income.get("bonus"))
        return total_income


a = Position()
a.get_full_name(a.name, a.surname)
print(a.position)
print(a._income)
print(a.get_total_income(a._income))

