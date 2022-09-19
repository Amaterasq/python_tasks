'''
Напишите декоратор кеширования к функции func,
который будет кешировать значения повторяющихся
вызовов функции func и возвращать результат без вычисления.
'''


def cached(func):
    cache = {}

    def wrap(arg):
        # nonlocal cache
        if not cache.get(arg):
            g = func(arg)
            cache[arg] = g
            return g
        else:
            return cache[arg]
    return wrap


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
