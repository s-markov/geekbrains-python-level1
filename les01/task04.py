input_num = int(input("Введите целое положительное число >>>"))
if input_num < 0:
    print("Неправильный ввод")
else:
    max_digit = input_num % 10
    current_num = input_num // 10
    while current_num > 0:
        if current_num % 10 > max_digit:
            max_digit = current_num % 10
        current_num = current_num // 10
    else:
        print(f"максимальная цифра числа {input_num} равна {max_digit}")
