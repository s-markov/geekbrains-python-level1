# Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    input_date: str

    def __init__(self, input_date: str):
        self.input_date = input_date

    @classmethod
    def date_to_num(cls, content):
        cls.result_list=[]
        for temp_str in content.split('-'):
            cls.result_list.append(int(temp_str))
        return cls.result_list

    @staticmethod
    def validate(content):
        content=Date.date_to_num(content)
        if not (content[1] in [1,3,5,7,8,10,12] and 0 < content[0] < 31) or (content[1] in [4.6,9,11] and 0 < content[0] < 30) or (content[1] == 2 and 0 < content[0] < 28) or (0>=content[2]):
            return f'Некорректный ввод элементов даты\n'
        else:
            return f'Все правильно: Дата={content[0]}  месяц={content[1]}  год={content[2]}\n'



print(Date.date_to_num('01-01-2020'))
print(Date.validate('01-01-2020'))

print(Date.date_to_num('32-01-2020'))
print(Date.validate('32-01-2020'))
