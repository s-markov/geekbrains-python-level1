# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class Complex(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '%s + %s*i' % (self.a, self.b)

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a-self.b*other.b, self.a*other.b + self.b*other.a)


first=Complex(5, 7)
second=Complex(3, 4)
print(f"первое число: {first}")
print(f"второе число: {second}")
print(f'сумма комплексных чисел: {first+second}')
print(f'произведение комплексных чисел: {first*second}')