'''
Любимый вариант очереди Тимофея — очередь,
написанная с использованием связного списка.
Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:

- get() — вывести элемент, находящийся в голове очереди,
и удалить его. Если очередь пуста, то вывести «error».
- put(x) — добавить число x в очередь
- size() — вывести текущий размер очереди

Формат ввода:
В первой строке записано количество команд n — целое число,
не превосходящее 1000. В каждой из следующих n строк записаны
команды по одной строке.

Формат вывода:
Выведите ответ на каждый запрос по одному в строке.
'''


class QueueList:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        self.queue.append(x)
        self.size += 1

    def get(self):
        if self.is_empty():
            return 'error'
        x = self.queue.pop(0)
        self.size -= 1
        return x


count_actions = int(input())
q = QueueList()

for i in range(count_actions):
    method = input().split(' ')
    if method[0] == 'get':
        print(q.get())
    elif method[0] == 'put':
        num = int(method[1])
        q.put(num)
    elif method[0] == 'size':
        print(q.size)
