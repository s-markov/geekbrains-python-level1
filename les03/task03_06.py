# Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().
#

def int_func(word):
    word = word.capitalize()
    return word


print(int_func("text"))

total_sum = 0
user_input = input(f"Введите сироку из слов в нижнем регистре, разделенные пробелом>>>  ")
my_string = ""
for user_word in user_input.split():
    if user_word.isalpha() and user_word.islower():
        my_string = my_string + int_func(user_word) + " "
    else:
        print("ошибка ввода")
        raise SystemExit

print(my_string)
