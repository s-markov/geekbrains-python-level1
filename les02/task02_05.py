# Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

current_r_list = [11, 11, 4, 3, 2, 2, 1]
while True:
    try:
        print("Текущий рейтинг ", current_r_list)
        user_raiting = (input(f"Введите рейтинг - натуральное число (Ctrl+D для выхода из режима ввода)>>>  "))
        if user_raiting.isdigit():
            user_raiting = int(user_raiting)
            current_r_list.reverse()
            for i in current_r_list:
                if user_raiting <= i:
                    current_r_list.insert(current_r_list.index(i), user_raiting)
                    break
                else:
                    continue
            current_r_list.reverse()
            if user_raiting > current_r_list[0]:
                current_r_list.insert(0, user_raiting)
        else:
            print("ошибка ввода")
    except EOFError:
        break
