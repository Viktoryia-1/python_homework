# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке \
# (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep


def red(text):
    return f"\033[31m {text}"


def yellow(text):
    return f"\033[33m {text}"


def green(text):
    return f"\033[32m {text}"


class TrafficLight:
    color = "light color"

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                print(f"{red(TrafficLight.color)}")
                sleep(7.0)
                i += 1
            elif i == 1:
                print(f"{yellow(TrafficLight.color)}")
                sleep(3.0)
                i += 1
            else:
                print(f"{green(TrafficLight.color)}")
                sleep(3.0)
                i += 1


a = TrafficLight()
print(a.color)
a.running()