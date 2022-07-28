'''
Гоша реализовал структуру данных Дек,
максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно.
Но, если в деке было много элементов, программа работала очень долго.
Дело в том, что не все операции выполнялись за O(1).
Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода:
В первой строке записано количество команд n — целое число,
не превосходящее 100000.
Во второй строке записано число m — максимальный размер дека.
Он не превосходит 50000.
В следующих n строках записана одна из команд:

- push_back(value) – добавить элемент в конец дека.
Если в деке уже находится максимальное число элементов, вывести «error».
- push_front(value) – добавить элемент в начало дека.
Если в деке уже находится максимальное число элементов, вывести «error».
- pop_front() – вывести первый элемент дека и удалить его.
Если дек был пуст, то вывести «error».
- pop_back() – вывести последний элемент дека и удалить его.
Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Формат вывода:
Выведите результат выполнения каждой команды на отдельной строке.
Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
'''


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, item):
        if self.size == self.max_size:
            raise IndexError('<Deque is full>')
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, item):
        if self.size == self.max_size:
            raise IndexError('<Deque is full>')
        self.items[self.head] = item
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('<Deque is empty>')
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return self.items[self.tail]

    def pop_front(self):
        if self.is_empty():
            raise IndexError('<Deque is empty>')
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return self.items[self.head]


if __name__ == '__main__':
    count_actions = int(input())  # Число комманд
    deque = Deque(int(input()))  # Максимальный размер дека

    for _ in range(count_actions):  # ввод комманд
        command, *params = input().split()
        try:
            output = getattr(deque, command)(*params)
            if output is not None:
                print(output)
        except IndexError:
            print('error')
        except AttributeError:
            raise ValueError(f'<Command {command} is not supported>')
