'''
Гоша написал программу, которая сравнивает строки исключительно
по их хешам. Если хеш равен, то и строки равны.
Тимофей увидел это безобразие и поручил вам сломать
программу Гоши, чтобы остальным неповадно было.

В этой задаче вам надо будет лишь найти две различные строки,
которые для заданной хеш-функции будут давать одинаковое значение.

Гоша использует следующую хеш-функцию:
для a = 1000 и m = 123987123.
В данной задаче необходимо использовать в качестве значений
отдельных символов их коды в таблице ASCII.

Формат ввода:
В задаче единственный тест без ввода

Формат вывода:
Отправьте две строки, по одной в строке.
Строки могут состоять только из маленьких латинских букв
и не должны превышать в длину 1000 знаков каждая.
Код отправлять не требуется. Строки из примера использовать нельзя.

Получилось абы как, но работает
'''

# Пример:
# string = 'ezhgeljkablzwnvuwqvp'  # 47021983
# string2 = 'gbpdcvkumyfxillgnqrv'  # 47021983

import random


base = 1000
module = 123_987_123
string = 'ertfxe'


def polyhash(string):
    hash = 0
    for c in string:
        hash = hash * base + ord(c)
    return hash % module


def get_rand_string():
    str_alpha = 'qwertyuiopasdfghjklzcvbnm'
    str_alpha = list(str_alpha)
    random.shuffle(str_alpha)
    string = ''.join(
        [random.choice(str_alpha) for _ in range(random.randint(1, 10))]
    )
    return string


def same_polyhash(string):
    fst_polyhash = polyhash(string)  # int
    scnd_string = get_rand_string()  # str
    scnd_polyhash = polyhash(scnd_string)  # int
    while fst_polyhash != scnd_polyhash:
        scnd_string = get_rand_string()
        scnd_polyhash = polyhash(scnd_string)
    # return scnd_string, scnd_polyhash
    return string, scnd_string


print(same_polyhash(string))
