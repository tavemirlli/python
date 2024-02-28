# !/usr/local/bin/python
# coding: UTF-8
# Вариант 19. В матрице найти среднее арифметическое элементов последних двух столбцов.
import numpy as np
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print('Последние 2 столбца матрицы: ')
print(matrix[0,1], matrix[0,2])
print(matrix[1,1],matrix[1,2])
print(matrix[2,1], matrix[2,2])

last_column = len(matrix[0]) - 1 # находим индекст последнего столбца матрицы
second_last_column = len(matrix[0]) - 2 # находим индекс предпоследнего столбца матрицы

last_two_columns = lambda row: row[last_column] + row[second_last_column] # создание функции lambda (сложение двух последних элементов в каждой строке матрицы)
average = sum(map(last_two_columns, matrix)) / (2 * len(matrix)) #  применение написанной функции к матрице и деление на количество элементов в 2 последних столбцах

print("Среднее арифметическое последних двух столбцов матрицы:", average)