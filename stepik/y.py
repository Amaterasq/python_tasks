# def increment_string(string: str) -> str:
#     if string[-1].isnumeric() and string[-1] != '0':
#         reverse_id = -2
#         while string[reverse_id].isnumeric():
#             reverse_id -= 1
#         return string[:reverse_id + 1] + str(int(string[reverse_id + 1:]) + 1)
#     return string + '1'


def increment_string(string: str) -> str:
    if string[-1].isnumeric():
        str_id = 1
        while string[str_id].isalpha() or string[str_id] == '0':
            str_id += 1
        return string[:str_id] + str(int(string[str_id:]) + 1)
    return string + '1'


assert increment_string('foo') == 'foo1'
assert increment_string('foobar23') == 'foobar24'
assert increment_string('foo0042') == 'foo0043'
assert increment_string('foo9') == 'foo10'
assert increment_string('foo099') == 'foo100'

