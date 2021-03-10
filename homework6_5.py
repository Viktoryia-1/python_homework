# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.t = title
        print(title)

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return f"Запуск отрисовки ручкой"


class Pencil(Stationery):
    def draw(self):
        return f"Запуск отрисовки карандашом"


class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки маркером"


first = Stationery("State")
print(first.draw())

a = Pen("Pen")
print(a.draw())

b = Pencil("Pencil")
print(b.draw())

c = Handle("Handle")
print(c.draw())