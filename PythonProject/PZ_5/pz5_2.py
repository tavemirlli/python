# Описать функцию ShiftLeft3(A,B,C), выполняющую левый циклический сдвиг: значение А переходит в С, значение С - в В,
# значение В - в А (А,В,С - вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой
# функции (ShiftLeft3(A,B,C)) выполнить левый циклический сдвиг для двух данных наборов из трех чисел (A1,B1,C1) и (A2,B2,c2).

# Описание функции ShiftLeft3(A,B,C)
def ShiftLeft3(A, B, C):
    A, B, C = B, C, A
    return A, B, C

A1 = input('Введите вещественное число A1: ')
while type(A1)!=float:
    try:
        A1 = float(A1)
    except ValueError:
        print('Неправильно ввели! ')
        A1 = input('Введите вещественное число A1: ')
B1 = input('Введите вещественное число B1: ')
while type(B1)!=float:
    try:
        B1 = float(B1)
    except ValueError:
        print('Неправильно ввели! ')
        B1 = input('Введите вещественное число B1: ')
C1 = input('Введите вещественное число C1: ')
while type(C1)!=float:
    try:
        C1 = float(C1)
    except ValueError:
        print('Неправильно ввели! ')
        C1 = input('Введите вещественное число C1: ')
A1, B1, C1 = ShiftLeft3(A1, B1, C1)
print(f"После сдвига для первого набора: A1 = {A1}, B1 = {B1}, C1 = {C1}")

A2 = input('Введите число A2: ')
while type(A1)!=float:
    try:
        A1 = float(A1)
    except ValueError:
        print('Неправильно ввели! ')
        A1 = input('Введите вещественное число A1: ')
B2 = input('Введите число B2: ')
while type(B2)!=float:
    try:
        B2 = float(B2)
    except ValueError:
        print('Неправильно ввели! ')
        B2 = input('Введите вещественное число B2: ')
C2 = input('Введите число C2: ')
while type(A1)!=float:
    try:
        С2 = float(A1)
    except ValueError:
        print('Неправильно ввели! ')
        С2 = input('Введите вещественное число A1: ')
A2, B2, C2 = ShiftLeft3(A2, B2, C2)
print(f"После сдвига для второго набора: A2 = {A2}, B2 = {B2}, C2 = {C2}")
