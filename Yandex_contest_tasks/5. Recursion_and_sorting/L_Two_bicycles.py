'''
Вася решил накопить денег на два одинаковых велосипеда — себе
и сестре. У Васи есть копилка, в которую каждый день он может
добавлять деньги (если, конечно, у него есть такая финансовая
возможность). В процессе накопления Вася не вынимает деньги
из копилки.
У вас есть информация о росте Васиных накоплений — сколько
у Васи в копилке было денег в каждый из дней.
Ваша задача — по заданной стоимости велосипеда определить
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода:
В первой строке дано число дней n, по которым велись наблюдения
за Васиными накоплениями. 1 ≤ n ≤ 106.
В следующей строке записаны n целых неотрицательных чисел.
Числа идут в порядке неубывания. Каждое из чисел не превосходит 106.
В третьей строке записано целое положительное
число s — стоимость велосипеда. Это число не превосходит 106.

Формат вывода:
Нужно вывести два числа — номера дней по условию задачи.
Если необходимой суммы в копилке не нашлось,
нужно вернуть -1 вместо номера дня.
'''


def binary_seach(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x and arr[mid - 1] < x or mid == 0:
        return mid + 1
    elif x <= arr[mid]:
        return binary_seach(arr, x, left, mid)
    else:
        return binary_seach(arr, x, mid + 1, right)


days = int(input())
arr = list(map(int, input().split()))
x = int(input())

print(binary_seach(arr, x, left=0, right=days), end=' ')


print(binary_seach(arr, x * 2, left=0, right=days))
