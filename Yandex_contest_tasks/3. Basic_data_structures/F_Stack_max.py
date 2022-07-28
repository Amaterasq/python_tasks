'''
Нужно реализовать класс StackMax, который поддерживает
операцию определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x), где x – целое число,
pop() и get_max().

Формат ввода:
В первой строке записано одно число n — количество команд,
которое не превосходит 10000. В следующих n строках идут команды.
Команды могут быть следующих видов:

- push(x) — добавить число x в стек;
- pop() — удалить число с вершины стека;
- get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None»,
для команды pop() — «error».

Формат вывода:
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
'''


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.items == []:
            return print('error')
        return self.items.pop()

    def get_max(self):
        if self.items == []:
            return print('None')
        return print(max(self.items))


stack = StackMax()

cnt_commands = int(input())
for i in range(cnt_commands):
    command = input().split()
    if len(command) == 2:
        eval('stack.{}({})'.format(command[0], command[1]))
    else:
        eval('stack.{}()'.format(command[0]))
