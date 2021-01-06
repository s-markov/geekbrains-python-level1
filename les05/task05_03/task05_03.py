#  Создать текстовый файл (не программно),
#  построчно записать фамилии сотрудников и величину их окладов
#  (не менее 10 строк).
#  Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#  вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.
from statistics import mean

my_file = open(r"task05_03.txt", 'r')
my_file_dict = {str_word.strip('\n').split(' ')[0]: float(str_word.strip('\n').split(' ')[1]) for str_word in
                my_file.readlines()}
my_file.close()
print(my_file_dict)
print('_____')
print('Список сотрудников с доходом менее 20000:')
for key, salary in my_file_dict.items():
    if salary < 20000:
        print(key, salary)
print('_____')
print(f'Средняя зарплата всех сотрудников : {round(mean(value for value in my_file_dict.values()), 2)}')
