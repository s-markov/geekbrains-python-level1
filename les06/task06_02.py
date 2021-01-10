# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.

# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int
    _numbers_of_layers: int
    __unit_weigth: int

    def __init__(self, num_of_layers=1):
        self._length = int(input('Введите длину дороги в метрах >>>'))
        self._width = int(input('Введите ширину дороги в метрах >>>'))
        self._numbers_of_layers = num_of_layers
        self.__unit_weigth = 25

    def road_weigth(self):
        road_weigth = self._length * self._width * self.__unit_weigth * self._numbers_of_layers / 1000
        print(f'Для покрытия полотна дороги необходимо {road_weigth} т асфальта')


road = Road(5)
road.road_weigth()
