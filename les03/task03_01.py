# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return

dividend = float(input("введите делимое >>>"))
divider = float(input("введите делитель >>>"))
if division(dividend, divider) == None:
    print("Делитель не может быть равен 0")
else:
    print("Частное = ", division(dividend, divider))
