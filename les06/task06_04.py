# Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    speed: int
    color: str
    name: str
    __is_police: bool
    direction: str

    def __init__(self, speed, color, name, direction="Прямо"):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.turn(direction)

    def turn(self, direction):
        if self.direction == "Направо":
            return ("Движение направо")
        elif self.direction == "Налево":
            return ("Движение налево")
        else:
            return ("Движение прямо")

    def go(self):
        return (f'{self.color} {self.name} поехала, {self.turn(self.direction)}')

    def stop(self):
        return (f'{self.color} {self.name} остановилась')

    def show_speed(self):
        return (f'{self.color} {self.name} Скорость = {self.speed}')

    def action(self):
        if not self.speed:
            print(self.stop())
        else:
            print(f'{self.go()}, {self.show_speed()}')


class TownCar(Car):
    speed: int
    color: str
    name: str
    __is_police = False
    direction: str

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return ('Превышен лимит скорости 60')


class SportCar(Car):
    speed: int
    color: str
    name: str
    __is_police = False
    direction: str


class WorkCar(Car):
    speed: int
    color: str
    name: str
    __is_police = False
    direction: str

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return ('Превышен лимит скорости 40')


class PoliceCar(Car):
    speed: int
    color: str
    name: str
    __is_police = True
    direction: str


volvo = TownCar(70, "Зеленый", "Вольво")
ferrari = SportCar(120, 'Красный', "Ferrari")
ford = PoliceCar(0, 'Синий', 'Форд', 'Направо')
suzuki = WorkCar(41, 'Оранжевый', 'Сузуки', 'Налево')

volvo.action()
ferrari.action()
ford.action()
suzuki.action()
