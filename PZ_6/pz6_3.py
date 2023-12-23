# Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию. Сделать список
# упорядоченным, переместив последний элемент на новую позицию.
from random import randint
list2 = []
N = input('Введите длину списка: ')
while type(N)!=int:
    try:
        N = int(N)
    except ValueError:
        print('Неправильно ввели! ')
        N = (input('Введите целое число: '))
for i in range (N):
    list2.append(randint(1,100))
print('Неотсортированный список: ', list2)
new_element = list2[-1]
sorted_list = sorted(list2[:-1])
sorted_list1 = sorted(list2[:-1])
sorted_list1.insert(N, new_element)
print('Упорядоченный список с последним элементом не на своем месте: ',sorted_list1)
index = 0
while index < len(sorted_list) and sorted_list[index] < new_element:
    index += 1
sorted_list.insert(index, new_element)
print("Упорядоченный список с последним элементом на новой позиции:", sorted_list)
