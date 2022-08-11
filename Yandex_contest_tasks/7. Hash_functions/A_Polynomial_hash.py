'''
Алле очень понравился алгоритм вычисления полиномиального хеша.
Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений
отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:
h(s) = (s1a^n-1 + s2a^n-2 + s3a^n-3...) mod m

Формат ввода:
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание,
по которому считается хеш.
Во второй строке дано число m (1 ≤ m ≤ 109) –— модуль.
В третьей строке дана строка s (0 ≤ |s| ≤ 106),
состоящая из больших и маленьких латинских букв.

Формат вывода:
Выведите целое неотрицательное число –— хеш заданной строки.
'''


def polyhash(base, module, string):
    hash = 0
    for c in string:
        hash = hash * base + ord(c)
    return hash % module


# print(polyhash(int(input()), int(input()), input()))

assert polyhash(123, 100003, 'a') == 97
assert polyhash(123, 100003, 'hash') == 6080
assert polyhash(123, 100003, 'HaSH') == 56156
