# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: см. в методичке.
#
# Следующий шаг — реализовать перегрузку метода str()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации
# операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            print(row)
        return ''

    def __add__(self, other):
         result = []
         for i in range(len(self.matrix)):
             temp_result = []
             for j in range(len(self.matrix[0])):
                 temp_result.append(self.matrix[i][j] + other.matrix[i][j])
             result.append(temp_result)
         return result



a = Matrix([[0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0], [0, 5, 1, 4, 2, 3]])
b = Matrix([[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]])

print('Матрица в привычном виде:')
print(a)
print('\nСумма двух матриц в привычном виде:')
print(Matrix(a + b))
