'''
Напишите функцию, которая принимает арабское число
и возвращает это же число римскими цифрами.
'''


def to_roman_numeral(num):
    lookup = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]
    res = ''
    for (arab_num, roman_num) in lookup:
        (remainder, num) = divmod(num, arab_num)
        res += roman_num * remainder
    return res


assert to_roman_numeral(3) == 'III'
assert to_roman_numeral(11) == 'XI'
assert to_roman_numeral(1998) == 'MCMXCVIII'
