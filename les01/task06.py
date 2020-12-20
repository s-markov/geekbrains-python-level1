# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_distance = int(input("Введите расстояние в км пробежки в первый день >>>"))
result_distance = int(input("Введите целевое расстояние пробежки, км не менее >>>"))
incr = 0.1
if first_distance <= 0 or result_distance <= first_distance:
    print("Неправильный ввод")
else:
    day_count = 1
    current_distatce = first_distance
    while current_distatce < result_distance:
        print(f"{day_count}-й день: {current_distatce} км")
        current_distatce += current_distatce * incr
        day_count += 1
    else:
        print(f"{day_count}-й день: {current_distatce} км")
    print(f"Ответ: на {day_count}-й день спортсмен достиг результата — не менее {result_distance} км.")
