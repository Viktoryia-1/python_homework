# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class MyDate:
    def __init__(self, string):
        self.date = string

    @classmethod
    def date(cls, obj):
        obj = obj.date.split('.')
        for el in obj:
            el = int(el)
        return f"День: {obj[0]} Месяц: {obj[1]} Год: {obj[2]}"

    @staticmethod
    def final(string):
        day, month, year = map(int, string.split("."))
        if day <= 31 and month <= 12 and year <= 2021 and year >= 1900:
            return f"Ваша дата {day} {month} {year} "
        else:
            return f"Дата введена неверно"


a = MyDate("10.10.1998")
print(MyDate.date(a))
print(MyDate.final("12.10.2000"))
print(a.final("23.12.1785"))

