#  Создать (не программно) текстовый файл со следующим содержимым:
#
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
my_en_ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
output_file_dict={}
my_file = open(r"task05_04.txt", 'r')
output_file = open(r"out05_04.txt", 'w')
my_file_dict = {str_word.split()[0]: str_word.strip('\n').split()[2] for str_word in my_file.readlines()}
print(my_file_dict)
for en_key, en_value in my_file_dict.items():
    for en_ru_key, ru_value in my_en_ru_dict.items():
        if en_key == en_ru_key:
            output_file_dict[ru_value] = en_value
print(output_file_dict)
for ru_key, ru_value in output_file_dict.items():
    output_file.write(f'{ru_key} - {ru_value}\n')
my_file.close()
output_file.close()
