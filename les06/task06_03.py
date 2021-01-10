# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться
# на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, income=None):
        if income is None:
            income = {"wage": 100000, "bonus": 30000}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def fullname(self):
        return f"{self.name} {self.surname}"

    def total_income(self):
        t_income = 0
        for self.key in self._income:
            t_income += sum(self._income[self.key])
        return t_income


class Position(Worker):
    name: str
    surname: str
    position: str
    _income: dict

    def get_full_name(self):
        return self.fullname()

    def get_total_income(self):
        return self.total_income()


engineer = Position("John", "Brown", "Leader Engineer", {"wage": [100000, 97000], "bonus": [30000, 25000]})
print(f'{engineer.fullname()}  {engineer.total_income()}')

print (f'{engineer.name},   {engineer.surname},   {engineer.position},   {engineer._income}')

