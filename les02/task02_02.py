# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
current_index = 0
while True:
    try:
        my_list.append(input(f"Введите {current_index}-й элемент списка (Ctrl+D для выхода из режима ввода)>>>  "))
        current_index += 1
    except EOFError:
        break
print(my_list)
new_list = my_list
for i in range(0, len(new_list)-1, 2):
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
print(new_list)


