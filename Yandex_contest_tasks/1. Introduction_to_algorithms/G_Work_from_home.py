'''
Вася реализовал функцию, которая переводит целое
число из десятичной системы в двоичную.
Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу
чисел в бинарное представление.

Формат ввода:
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода:
Выведите двоичное представление этого числа.
'''


def binary(n):
    number = ''
    while n > 0:
        number = str(n % 2) + number
        n //= 2
    return number


# print(binary(int(input())))


assert binary(14) == '1110'
assert binary(5) == '101'
