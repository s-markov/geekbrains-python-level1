# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birth, city, email, phone):
    return name + "  "+surname+"  "+birth+"  "+city+"  "+email+"  "+phone


print(user_data(name="John", birth="01.01.2001", surname="Brown", phone="+123456789", city="New York", email="name@mail.com"))
