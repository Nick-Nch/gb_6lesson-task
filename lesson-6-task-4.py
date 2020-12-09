# 4
# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def going(self):
        return f'{self.name} is riding'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} turning right'

    def turn_left(self):
        return f'{self.name} turning left'

    def show_speed(self):
        return f'{self.name} speed is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')
        if self.speed > 60:
            print('over speed!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')
        if self.speed > 40:
            print('over speed!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police Mayami'
        else:
            return f'{self.name} is not from police Mayami'


jaguar = SportCar(220, 'Red', 'Jaguar', False)
ford = PoliceCar(120, 'White', 'Ford', True)
nissan = TownCar(80, 'Black', 'Nissan', False)
bmw = WorkCar(35, 'Green', 'BMW', False)

print(jaguar.show_speed())
print(jaguar.turn_left())
print(ford.police())
print(nissan.show_speed())