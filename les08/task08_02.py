# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

from random import randint

class OwnDevideToZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = randint(0, 100)
print(f' Делимое = {dividend}')
divider = input("Введите делитель>>> ")

try:
    divider_data = int(divider)
    if divider_data == 0:
        raise OwnDevideToZero("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnDevideToZero as err:
    print(err)
else:
    print(f"Все хорошо. Частное: {dividend/divider_data}")
