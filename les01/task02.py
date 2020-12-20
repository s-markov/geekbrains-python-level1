time_input_sec = int(input("Введите время в секундах (целое положительное число не более 359999)>>>"))
if 0 <= time_input_sec <= 359999:
    time_hour = time_input_sec // 3600
    time_hour_dec = time_hour // 10
    time_hour_num = time_hour % 10
    time_min = (time_input_sec - (time_hour * 3600)) // 60
    time_min_dec = time_min // 10
    time_min_num = time_min % 10
    time_sec = (time_input_sec - (time_hour * 3600) - (time_min * 60))
    time_sec_dec = time_sec // 10
    time_sec_num = time_sec % 10
    print(
        f"{time_input_sec} секунд - это {time_hour_dec}{time_hour_num}:{time_min_dec}{time_min_num}:{time_sec_dec}{time_sec_num} в формате чч:мм:сс")
else:
    print("Неправильный ввод")
