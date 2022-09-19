'''
Дана строка (неизменяемый тип). Нужно вернуть перевернутую.
'''

s = 'Кошка'


def reverse_string(string):
    return s[::-1].capitalize()


print(reverse_string(s))
