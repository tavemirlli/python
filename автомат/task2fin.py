from random import randint
a = []
n = 29
for i in range(0, n):
    a.append(randint(0,10000))\

x = randint(1, 99)

if x % 5 == 0:
    x = x - 1

a.append(x)

print('исходный массив: ')
for i in range(0, len(a)):
    print(a[i])

j = len([i for i in a if i < 100 and i % 5 != 0])

for i in range (0, len(a)):
    if a[i] < 100 and a[i] % 5 != 0:
        a[i] = j

print('\n''Изменненый массив: ')

for i in a:
    print(i)

