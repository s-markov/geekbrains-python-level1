input_num = int(input("Введите целое положительное число от 0 до 9>>>"))
if 0 <= input_num < 10:
    result_num = input_num * (1 + 11 + 111)
    print("Результат = {}".format(result_num))
else:
    print("Неправильный ввод")
