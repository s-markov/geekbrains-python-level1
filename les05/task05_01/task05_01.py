# Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует
# пустая строка.


my_file = open(r"task05_01.txt", 'w+')
if not my_file.writable():
    print("Can not write")
else:
    while True:
        input_str = input(f"Введите строку текста (Enter для выхода)>>>  ")
        if input_str != "":
           my_file.write(f'{input_str}\n')
        else:
            break
my_file.seek(0)
print(my_file.read())
my_file.close()
