# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
#
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

for el in count(3):
    if el > 12:
        break
    else:
        print(el)
print('Done count()')

с = 0
cycle_count = ["one", "two", "three", "four"]
for el in cycle(cycle_count):
    if с > 15:
        break
    print(el)
    с += 1
print('Done cycle()')
