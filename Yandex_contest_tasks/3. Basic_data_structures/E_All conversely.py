'''
Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные.
Нужно написать только функцию, которая принимает на вход голову
двусвязного списка и возвращает голову перевёрнутого списка.
Ниже дано описание структуры, которая задаёт вершину списка.

Формат ввода:
Функция принимает на вход единственный аргумент — голову двусвязного списка.
Длина списка не превосходит 1000 элементов. Список не бывает пустым.

Формат вывода:
Функция должна вернуть голову развернутого списка.
'''


'''
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
'''


def solution(node):
    while node:
        # print(node.value)
        node.prev, node.next = node.next, node.prev
        if node.prev is not None:
            node = node.prev
        else:
            return node


'''
def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1


test()
'''
