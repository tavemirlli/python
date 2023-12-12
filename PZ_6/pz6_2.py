# Дан целочисленный список размера N. Найти количество различных элементов(не одинаковых) в данном списке.
from random import randint
list1 = []
N = input('Введите размер списка: ')
while type(N)!=int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели! ')
        N = (input('Введите целое число: '))
for i in range(N):
    list1.append(randint(1,100))
print(list1)
uniq = set(list1)
a = len(uniq)
print('Количество уникальных элементов: ',a)