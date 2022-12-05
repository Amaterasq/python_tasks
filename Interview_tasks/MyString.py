'''
Реализовать класс MyString,
который будет поддерживать операцию вычитания из строки.
Если исходная строка (a) начинается с указанной для вычета строки (b),
вернуть строку a без подстроки b
Если нет - вернуть исходную строку.
Возвращать нужно объект MyString

Пример:
a = MyString('abcd')
b = 'ab'
print(a - b) -> cd
'''


class MyString(str):
    def __init__(self, a):
        self.a = a

    def __sub__(self, b):
        if self.a.startswith(b):
            return MyString(self.a.replace(b, '', 1))
        return MyString(self.a)


test_string = MyString('aabcdefghijklmn')

# Работа со строками
assert test_string - 'aabc' == 'defghijklmn'
# Работа с объектом класса
assert test_string - MyString('aabc') == MyString('defghijklmn')
# Замена только первого вхожения
assert test_string - 'a' == 'abcdefghijklmn'
assert test_string - MyString('a') == 'abcdefghijklmn'
# Если подстрока не входит в строку
assert test_string - 'xyz' == 'aabcdefghijklmn'
