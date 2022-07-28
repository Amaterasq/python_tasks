'''
Тимофей записал два числа в двоичной системе счисления
и попросил Гошу вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения
двоичных чисел применять нельзя. Помогите Гоше решить задачу.

Решение должно работать за O(N),
где N –— количество разрядов максимального числа на входе.

Формат ввода:
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

Формат вывода:
Одно число в двоичной системе счисления.
'''


def binary_sum(num1, num2):
    num1, num2 = list(map(int, num1)), list(map(int, num2))
    num1, num2 = num1[::-1], num2[::-1]
    size = max(len(num1), len(num2))
    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))
    overflow = 0
    res = []
    for obj in zip(num1, num2):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)
    if overflow == 1:
        res.append(1)
    res = res[::-1]
    return ''.join(map(str, res))


# print(binary_sum(input(), input()))

assert binary_sum('1010', '1011') == '10101'
assert binary_sum('1', '1') == '10'
