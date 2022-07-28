'''
Астрологи объявили день очередей ограниченного размера.
Тимофею нужно написать класс MyQueueSized, который принимает
параметр max_size, означающий максимально допустимое количество
элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать
работу такой очереди. Функции, которые надо поддержать,
описаны в формате ввода.

Формат ввода:
В первой строке записано одно число — количество команд,
оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди,
он не превосходит 5000.
Далее идут команды по одной на строке.
Команды могут быть следующих видов:

- push(x) — добавить число x в очередь;
- pop() — удалить число из очереди и вывести на печать;
- peek() — напечатать первое число в очереди;
- size() — вернуть размер очереди;

При превышении допустимого размера очереди нужно вывести «error».
При вызове операций pop() или peek() для пустой очереди
нужно вывести «None».

Формат вывода:
Напечатайте результаты выполнения нужных команд, по одному на строке.
'''


class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


count_actions = int(input())
q = Queue(int(input()))

for i in range(count_actions):
    method = input().split(' ')
    if method[0] == 'pop':
        print(q.pop())
    elif method[0] == 'peek':
        print(q.peek())
    elif method[0] == 'push':
        num = int(method[1])
        q.push(num)
    elif method[0] == 'size':
        print(q.size)
