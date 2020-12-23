# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = {"Зима": (1, 2, 12), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
month_num = input("Введите номер месяца (от 1 до 12) >>> ")
if month_num.isdigit() and 1 <= int(month_num) <= 12:
    month_num = int(month_num)
    # Метод list
    if month_num < 12:
        result_season_l = seasons_list[month_num // 3]
    else:
        result_season_l = seasons_list[0]
    print(f"По методу 'list' время года {month_num}-го месяца  - {result_season_l}")

    # Метод dict
    for key in seasons_dict.keys():
        if month_num in seasons_dict[key]:
            print(f"По методу 'dict' время года {month_num}-го месяца  - {key}")
else:
    print('ошибка ввода')
