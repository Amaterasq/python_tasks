'''
Тимофей решил купить несколько домов на знаменитом
среди разработчиков Алгосском архипелаге.
Он нашёл n объявлений о продаже, где указана
стоимость каждого дома в алгосских франках.
А у Тимофея есть k франков. Помогите ему определить,
какое наибольшее количество домов на Алгосах он сможет
приобрести за эти деньги.

Формат ввода:
В первой строке через пробел записаны натуральные числа n и k.
n — количество домов, которые рассматривает Тимофей,
оно не превосходит 100000;
k — общий бюджет, не превосходит 100000;
В следующей строке через пробел записано n стоимостей домов.
Каждое из чисел не превосходит 100000. Все стоимости — натуральные числа.

Формат вывода:
Выведите одно число —– наибольшее количество домов,
которое может купить Тимофей.
'''


count_houses, cash = list(map(int, input().split()))
prices = list(map(int, input().split()))


def max_houses(count_houses, cash, prices):
    prices.sort()
    houses = 0
    for price in prices:
        if price > cash:
            return houses
        else:
            cash -= price
            houses += 1
    return houses


print(max_houses(count_houses, cash, prices))
