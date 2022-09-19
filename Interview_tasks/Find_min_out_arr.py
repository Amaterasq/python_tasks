'''
Дан массив из n натуральных чисел.
Нужно найти минимальное натуральное число не в этом массиве.
[1, 2, 5, 15, 10] => 3
'''

from typing import List


arr = [1, 2, 5, 15, 10]

'''
def find_min_out(array):  # Без сортировки
    if min(array) > 1:
        return 1
    for num in array:
        if num + 1 not in array:
            return num + 1
'''


def find_min_out(array: List[int]) -> int:  # За линейное время
    if not array:
        return 1
    array = set(array)
    current = 1
    while True:
        if current not in array:
            return current
        current += 1


print(find_min_out([1, 2, 5, 15, 10]))
print(find_min_out([2, 5, 15, 10]))
print(find_min_out([]))

# assert find_min_out([1, 2, 5, 15, 10]) == 3
# assert find_min_out([1, 2, 3, 4, 5]) == 6
