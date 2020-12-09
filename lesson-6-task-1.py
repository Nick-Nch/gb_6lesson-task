# 1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
import time

class TrafficLight:

    def __init__(self):
        print('Begining')
        self.__running()
        self.__color()

    def __color(self):
        while True:
            time.sleep(2)
            print('Red')
            time.sleep(7)
            print('Yellow')
            time.sleep(2)
            print('Green')
            time.sleep(8)

    def __running(self):
        time.sleep(2)
        print('Working')

g_r_y = TrafficLight()
print(g_r_y)
