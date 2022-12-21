'''
Напишите функцию с именем first_non_repeating_letter,
которая принимает на вход строку и возвращает первый символ,
который нигде в строке не повторяется.
Например, при вводе 'stress'функция должна вернуть 't'значение,
так как буква t встречается в строке только один раз и встречается
первой в строке.
В качестве дополнительной проблемы прописные и строчные буквы считаются
одним и тем же символом , но функция должна возвращать правильный регистр
для начальной буквы. Например, ввод 'sTreSS'должен возвращать 'T'.
Если строка содержит все повторяющиеся символы, она должна возвращать
пустую строку ("") или None -- см. примеры тестов.
'''


def first_non_repeating_letter(string: str):
    for i in string:
        if i.isalpha():
            if string.count(i.lower()) + string.count(i.upper()) == 1:
                return i
        elif not i.isalpha():
            if string.count(i) == 1:
                return i
    return ''


# def first_non_repeating_letter(string):
#     singles = [i for i in string if string.lower().count(i.lower()) == 1]
#     return singles[0] if singles else ''


print(first_non_repeating_letter('sTreSS'))
