#  Создать текстовый файл (не программно),
#  сохранить в нем несколько строк,
#  выполнить подсчет количества строк,
#  количества слов в каждой строке.
num_str=0
my_file = open(r"task05_02.txt", 'r')
for str_word in my_file.readlines():
    num_word = 0
    for word in str_word.split(' '):
        if word.isalpha():
            num_word +=1
    num_str+=1
    print(f'строка {num_str}:   {num_word} слов')
print(f'всего строк: {num_str}')
my_file.close()
