# Вариант 19. Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность
# из целых положительных и целых отрицательных чисел. Сформировать новый файл (.txt) следующего вида,
# предворительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы до n-1 умножены на элемент n:

from random import randint
numbers = []
n = int(input('Введите количество элементов: '))
for i in range(n):
    numbers.append(randint(-10,10))
print(numbers)
sum_numbers = sum(numbers)
print('Сумма элементов: ', sum_numbers)


# умножаем элементы последовательности
result_umn = []
numbers1 = numbers[:-1]
# print(numbers1)
for i in range(0, len(numbers1)):
    result_umn.append(numbers1[i] * numbers[-1])
print('Элементы до n-1 умножены на элемент n: ', result_umn)



with open('pz11_1file.txt', 'w') as file:
    file.write(f'Исходные данные: {numbers}\n',)
    file.write(f'Количество элементов: {n}\n')
    file.write(f'Сумма элементов: {sum_numbers}\n')
    file.write(f'Элементы до n-1 умножены на элемент n: {result_umn}\n')

print('Файл pz11_1file.txt успешно создан.')