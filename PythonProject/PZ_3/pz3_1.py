# Вариант 19. Проверить истинность высказывания: "Среди данных трех целых чисел есть хотя бы одна пара совпадающих"while type(a) != int:try:
a = (input('Введите первое число: '))
while type(a)!=int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели! ')
        a = (input('Введите первое число: '))
b = (input('Введите второе число: '))
while type(b)!=int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели!')
        b = (input('Введите второе число: '))
c = (input('Введите третье число: '))
while type(c)!=int:
    try:
        c = int(c)
    except ValueError:
        print('Неправильно ввели!')
        c = (input('Введите третье число: '))
ab = a == b
bc = b == c
ac = a == c
abc = ab or bc or ac
print("a равно b: ", ab)
print("b равно c: ", bc)
print("a равно c: ", ac)
print('Есть одна пара совпадающих чисел: ', abc)
