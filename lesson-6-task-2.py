# 2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width



class RequiredMass(Road):
    def __init__(self, _length, _width, vol, weight):
        self.vol = vol
        self.weight = weight
        super().__init__(_length, _width)

    def result(self):
        return self._length * self._width * self.weight * self.vol



el = RequiredMass(5000, 20, 0.05, 25)
print(el.result())