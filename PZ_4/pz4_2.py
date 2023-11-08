# Дано целое число N (>0). Найти сумму 1^1+2^2+…+N^N.


N = input('Введите целое число: ')
S = 0
while type(N) != int:
     try:
         N = int(N)
     except ValueError:
        print('Неправильно ввели!')
        N = input('Введите целое число: ')
for N in range(1, N+1):
    S += N ** N

print('Cумма членов: ', S)