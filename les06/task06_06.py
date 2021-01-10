# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    title: str

    def draw(self):
        super().draw()
        print(f'{self.title} - это ручка')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} - это карандаш')


class Handle(Stationery):
   def draw(self):
       super().draw()
       print(f'{self.title} - это маркер')

#pen = Stationery('Koh-i-Noor')  - если все методы базового класса переопределены
       # - невозможно напрямую вызвать базовый класс
pen = Pen('Koh-i-Noor')
pencil = Pencil('STABILO')
handle = Handle('Sketchmarker')

pen.draw()
pencil.draw()
handle.draw()
