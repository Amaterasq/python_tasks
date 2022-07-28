'''
Представьте себе онлайн-игру для поездки в метро:
игрок нажимает на кнопку, и на экране появляются три случайных числа.
Если все три числа оказываются одной чётности, игрок выигрывает.
Напишите программу, которая по трём числам определяет, выиграл игрок или нет.

Формат ввода:
В первой строке записаны три случайных целых числа a, b и c.
Числа не превосходят 109 по модулю.

Формат вывода:
Выведите «WIN», если игрок выиграл, и «FAIL» в противном случае.
'''


def parity(numbers):
    res = [True if num % 2 == 0 else False for num in numbers]
    if res == [True, True, True] or res == [False, False, False]:
        return 'WIN'
    return 'FAIL'


def parity_case(numbers):  # only for python 3.10+
    match [True if num % 2 == 0 else False for num in numbers]:
        case [True, True, True]:
            return 'WIN'
        case [False, False, False]:
            return 'WIN'
    return 'FAIL'


# print(parity2(list(map(int, input().split()))))


assert parity([1, 2, -3]) == 'FAIL'
assert parity([7, 11, 7]) == 'WIN'
assert parity([6, -2, 0]) == 'WIN'

assert parity_case([1, 2, -3]) == 'FAIL'
assert parity_case([7, 11, 7]) == 'WIN'
assert parity_case([6, -2, 0]) == 'WIN'
