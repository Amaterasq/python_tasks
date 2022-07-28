'''
Гоша любит играть в игру «Подпоследовательность»:
даны 2 строки, и нужно понять, является ли первая из них
подпоследовательностью второй. Когда строки достаточно длинные,
очень трудно получить ответ на этот вопрос, просто посмотрев на них.
Помогите Гоше написать функцию, которая решает эту задачу.

Формат ввода:
В первой строке записана строка s.
Во второй —- строка t.
Обе строки состоят из маленьких латинских букв,
длины строк не превосходят 150000.
Строки не могут быть пустыми.

Формат вывода:
Выведите True, если s является подпоследовательностью t, иначе —– False.
'''


def is_substring(substring, string):
    if not (substring and string):
        return True
    current = 0
    for char in string:
        if char == substring[current]:
            current += 1
        if current == len(substring):
            return True
    return False


print(is_substring(input(), input()))