'''
Реализуйте класс StackMaxEffective, поддерживающий операцию
определения максимума среди элементов в стеке.
Сложность операции должна быть O(1). Для пустого стека
операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода:
В первой строке записано одно число — количество команд,
оно не превосходит 100000. Далее идут команды по одной в строке.
Команды могут быть следующих видов:

- push(x) — добавить число x в стек;
- pop() — удалить число с вершины стека;
- get_max() — напечатать максимальное число в стеке;

Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».

Формат вывода:
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
'''


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_list = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if self.max_list == [] or self.max_list[-1] <= item:
            self.max_list.append(item)

    def pop(self):
        if self.items:
            if self.items[-1] == self.max_list[-1]:
                self.max_list.pop()
            return self.items.pop()
        print('error')

    def get_max(self):
        if self.items:
            print(self.max_list[-1])
        else:
            print('None')


stack = StackMaxEffective()

count_actions = int(input())
for i in range(count_actions):
    method = input().split(' ')
    if method[0] == 'pop':
        stack.pop()
    elif method[0] == 'get_max':
        stack.get_max()
    elif method[0] == 'push':
        num = int(method[1])
        stack.push(num)
