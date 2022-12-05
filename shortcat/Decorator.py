'''
Декораторы
'''


def add_something(decor_text):
    def decor_func(func):
        def wrap(*args, **kwargs):
            return f'{func(*args)} {decor_text}'
        return wrap
    return decor_func


@add_something(decor_text='Helo!')
def func(name):
    return f'Привет, {name}!'


print(func('Гоша'))
