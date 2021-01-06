#  Создать (программно) текстовый файл,
#  записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#
import random
from functools import reduce

my_file = open(r"task05_05.txt", "w+")
for i in range(20):
    my_file.write(f'{round(random.random() * 100, 2)} ')
my_file.seek(0)
print(round(reduce(lambda x, y: x + y, list(map(float, my_file.read().split()))), 2))
my_file.close()
