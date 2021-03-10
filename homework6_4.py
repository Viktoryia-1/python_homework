# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.n = name
        self.s = speed
        self.c = color
        self.p = is_police
        print(name, speed, color)

    def go(self):
        return f"Go car {self.n}"

    def stop(self):
        return f"Stop car {self.n}"

    def turn(self, way):

        if way == "left":
            return f"car {self.n} turn left"
        elif way == "right":
            return f"car {self.n} turn right"
        else:
            return f"car {self.n} turn {way}"

    def show_speed(self, speed):
        return f"car moves with speed {speed}"


class TownCar(Car):
    def show_speed(self, speed):
        if speed > 60:
            return f"car moves with speed {speed}, Attention! excessive speed on {speed - 60}"
        else:
            return f"car moves with speed {speed}"


class SportCar(Car):
    def sine(self, sine):
        print(f"{sine}")


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            return f"car moves with speed {speed}, Attention! excessive speed on {speed - 40}"
        else:
            return f"car moves with speed {speed}"


class PoliceCar(Car):
    def action(self,car_name, command):
        return f"Car {car_name}, {command}"


a = TownCar("Mazda", 40, "green")
print(a.go())
print(a.stop())
print(a.turn("left"))
print(a.show_speed(70))

b = SportCar("BMW", 85, "red")
print(b.go())
print(b.sine("VZZZZZ!"))
print(b.stop())
print(b.turn("left"))
print(b.show_speed(70))

c = WorkCar("lada", 65, "white")
print(c.go())
print(c.stop())
print(c.turn("left"))
print(c.show_speed(70))

d = PoliceCar("Mercedes", 120, "Black", True)
print(d.go())
print(d.stop())
print(d.turn("left"))
print(d.show_speed(70))
print(d.action("BMW", "stop!"))


