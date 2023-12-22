# Составить функцию решения задачи: из заданного числа вычли сумму его чисел. Из результата вновь вычли сумму его чисел
# и т.д. Через сколько таких действий получится нуль?
a = input('Введите целое число: ')
while type(a)!=int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели! ')
        a = (input('Введите целое число: '))
d = sum(map(int, str(a)))
s = 0
def func(a, d, s):
    while a > 0:
        a = a - d
        d = sum(map(int, str(a)))
        s += 1
    return s
m = func(a, d, s)

print('Количество действий: ', m)