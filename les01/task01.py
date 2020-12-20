current_year: int = 2020
current_month = "december"
current_date = 20
print(f"Today is {current_date} of {current_month}, {current_year}")

username = input("Укажите Ваше имя:")
year_of_birth = int(input("Укажите год своего рождения:"))
next_age = current_year - year_of_birth + 1
if 0 < next_age <= 5:
    print("{}, в следующем году Вам исполнится {} лет. Видимо, Вы - вундеркинд".format(username, next_age))
elif next_age > 5:
    print("{}, в следующем году Вам исполнится {} лет.".format(username, next_age))
else:
    print("Неправильно введен год рождения, год рождения должен быть меньше 2021")
