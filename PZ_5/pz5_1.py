# Составить функцию решения задачи: из заданного числа вычли сумму его чисел. Из результата вновь вычли сумму его чисел
# и т.д. Через сколько таких действий получится нуль?
a = input('Введите целое число: ')
while type(a)!=int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели! ')
        a = (input('Введите целое число: '))
def func(a):
    s = 0
    while a > 0:
        d = sum(map(int, str(a)))
        a = a - d
        s += 1
    return s
print('Количество действий: ', func(a))