# Дано вещественное число Х и целое число N (>0). Найти значение выражения Х - Х^3/(3!) +X^5/(5!) - ... +
# (-1)^(N)-X^(2*N+1)/((2*N+1)!) (N! = 12…N). Полученное число является приближенным значением функции sin в точке Х.
import math
X = input('Введите вещественное число: ')
while type(X) != float:
    try:
        X = float(X)
    except ValueError:
        print('Неправильно ввели!')
        X = input('Введите вещественное число: ')
I = input('Введите количество итераций: ')
while type(I) != int:
    try:
        I = int(I)
    except ValueError:
        print('Неправильно ввели!')
        I = input('Введите вещественное число: ')
def sin(X,I):
    S = 0
    for N in range(I):
        a = X ** (2 * N + 1)
        b = math.factorial(2 * N + 1)
        c = ((-1) ** N) * (a / b)
        S += c
    return S
print('Результат: ', sin(X,I))
print('Синус введенного числа: ', math.sin(X))
