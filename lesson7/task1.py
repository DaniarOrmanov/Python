# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом сложения
# должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:

    def __init__(self, mat_data):
        self.mat_data = mat_data

    def __str__(self):
        matrix = ''
        for i in self.mat_data:
            for j in i:
                matrix = matrix + str(j) + '  '
            matrix = str(matrix[0:len(matrix)-2]) + '\n'
        return str(matrix)

    def __add__(self, other):
        i = 0
        sum_m = self.mat_data
        while i < len(self.mat_data):
            j = 0
            while j < len(self.mat_data[1]):
                sum_m[i][j] = self.mat_data[i][j] + other.mat_data[i][j]
                j += 1
            i += 1
        return Matrix(sum_m)


a = [[-1, 2.5, 3], [4, -5, 6.5], [7, 8, 9], [-10, 11, 12]]
b = [[3, -2, 3.5], [-5, 6, -4], [-3.5, 6, 12], [-6.5, 1, 6.3]]

m1 = Matrix(a)
m2 = Matrix(b)

print(f'Первая матрица:\n{m1}')
print(f'Вторая матрица:\n{m2}')
print(f'Сумма двух матриц:\n{m1 + m2}')



