# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
#
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
#
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, n, c):
        self.name = n
        self.color = c
        self.dict = {}

    def take(self):
        my_keys = ["название", "цена", "количество", "еденицы измерения"]

        items_count = int(input("Введите количество товаров: "))
        values_options = []

        name = []
        cost = []
        count_list = []
        s = []

        while items_count != 0:
            items_count -= 1
            my_values = []
            values_options.append(my_values)
            for i in range(1):
                param = input("введите название")
                param_2 = input("введите цену")
                param_3 = input("введите количество")
                param_4 = input("введите еденицу измерения")
                my_values.append(param)
                my_values.append(param_2)
                my_values.append(param_3)
                my_values.append(param_4)

        for el in range(len(values_options)):
            name.append(values_options[el][0])
            cost.append(values_options[el][1])
            count_list.append(values_options[el][2])
            s.append(values_options[el][3])

        last_list = []
        count = len(values_options)
        start = 1

        while count != start:
            number = 1
            for el in values_options:
                my_dict = dict(zip(my_keys, el))
                my_dict = (number, my_dict)
                number += 1
                last_list.append(my_dict)
            start += 1
        my_dict = dict(название=name, цена=cost, количество=count_list, еденицы_измерения=s)
        self.dict.update(my_dict)

        return f"Сейчас на складе:\n {self.dict} \n"


class Printer(OfficeEquipment):
    def could_print(self):
        return f"It could print!!!"


class Xerox(OfficeEquipment):
    def copy(self):
        return f"It could copy!!!"


class Scanner(OfficeEquipment):
    def scan(self):
        return f"It could scan!!!"


a = Scanner("Canon", "black")
print(a.scan())
print(a.take())
b = Printer("Mac", "green")
print(b.could_print())
print(b.take())
print(a.dict)
