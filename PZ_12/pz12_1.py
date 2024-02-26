# !/usr/local/bin/python
# coding: UTF-8
# Вариант 19. В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.

numbers = []
n = int(input('Введите количество элементов последовательности: '))
numbers = [i for i in range (10)]
print('Сгенерированная последовательность:', numbers)
def average_first_third(number):
    n = len(numbers)
    first_third = numbers[:n // 3]  # первая треть последовательности
    print(first_third)
    avg = sum(first_third) / len(first_third) if len(first_third) > 0 else 0  # среднее арифметическое первой трети
    return avg

result = average_first_third(numbers)
print(result)

