# Дан список размера N и целые числа K и L (1<K<L<N). Найти сумму элементов списка с номерами от K до L включительно.
from random import randint
arr =[]
for i in range(10):
    arr.append(randint(10,100))
print(arr)
K = int(input('Элементы от : '))
L = int(input('Элементы до: '))
def sum_elements_in_range(arr, K, L):
    if 1 < K < L < len(arr):
        sum = 0
        for i in range(K-1, L):
            sum += arr[i]
        return sum
    else:
        return "Ошибка: 1 < K < L < N не выполняется"
result = sum_elements_in_range(arr, K, L)
print(f"Сумма элементов списка с номерами от {K} до {L} включительно: {result}")