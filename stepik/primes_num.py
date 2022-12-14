'''
Бесконечно возвращает простые числа через yeild
'''
import itertools


def is_prime(num):
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
    return True

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# Оптимизировано, меньше алгоритмическая сложность через
# корень значения и принимает отрицательные числа
# import math

# def is_prime(num):
#     if num < 0:
#         return False
#     if num == 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(num) + 1), 2):
#         if num % i == 0:
#             return False
#     return True

# n = primes()
# for i in range(100):
#     print(next(n))

print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]