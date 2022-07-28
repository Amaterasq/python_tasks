'''
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры,
заглавные и строчные буквы считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода:
В единственной строке записана фраза или слово.
Буквы могут быть только латинские.
Длина текста не превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв,
цифр, знаков препинания.

Формат вывода:
Выведите «True», если фраза является палиндромом, и «False», если не является.
'''


def is_palindrome(input_text):
    text = [i for i in input_text if i.isalpha()]  # or i.isnumeric()
    return text == text[::-1]
    # return ''.join(text) == ''.join(reversed(text))


# print(is_palindrome(input().lower()))


assert is_palindrome('a man, a plan, a canal: panama') is True
assert is_palindrome('zo') is False
