'''
Реализуйте решение:
chain_sum(5)() -> 5
chain_sum(5)(2)() -> 7
chain_sum(5)(100)(-10)() -> 95
'''


def chain_sum0(number):
    result = number

    def wrapper(number2=None):
        nonlocal result
        if number2 is None:
            return result
        result += number2
        return wrapper
    return wrapper


def chain_sum(number):  # Красивее код
    def wrapper(number2=None):
        if number2 is None:
            return wrapper.result
        wrapper.result += number2
        return wrapper
    wrapper.result = number
    return wrapper


class chain_sum_cls0:  # Будет работать без доп пустых скобок
    def __init__(self, number):
        self._number = number

    def __call__(self, value=0):
        return chain_sum_cls0(self._number + value)

    def __str__(self):
        return str(self._number)


class chain_sum_cls(int):  # Позволяет использовать результат в арифм операциях
    def __call__(self, addition=0):
        return chain_sum_cls(self + addition)


def main():
    print(chain_sum(5)())
    print(chain_sum(5)(2)())
    print(chain_sum(5)(100)(-10)())
    print(chain_sum(5)(100)(-10)(10)(100)())

    print(chain_sum_cls0(5)())
    print(chain_sum_cls0(5)(2)())
    print(chain_sum_cls0(5)(100)(-10)())

    print(1 + chain_sum_cls(5)())
    print(1 + chain_sum_cls(5)(2)())
    print(1 + chain_sum_cls(5)(100)(-10)())


if __name__ == '__main__':
    main()
