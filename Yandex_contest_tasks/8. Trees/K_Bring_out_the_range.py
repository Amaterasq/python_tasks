'''
Напишите функцию, которая будет выводить по неубыванию все ключи от
L до R включительно в заданном бинарном дереве поиска.
Ключи в дереве могут повторяться. Решение должно иметь сложность
O(h+k), где h –— глубина дерева, k — число элементов в ответе.
В данной задаче если в узле содержится ключ x,
то другие ключи, равные x, могут быть как в правом,
так и в левом поддереве данного узла.
(Дерево строил стажёр, так что ничего страшного).

Формат ввода:
На вход функции подаётся корень дерева и искомый ключ.
Число вершин в дереве не превосходит 105.
Ключи – натуральные числа, не превосходящие 109.
Гарантируется, что L≤R.
В итоговом решении не надо определять свою структуру / свой класс,
описывающий вершину дерева.

Формат вывода:
Функция должна напечатать по неубыванию все ключи от L до R
по одному в строке.

Решение рабочее, однако медленное (нужно сделать быстрее)
'''


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


# def print_range(node, left, right):  # центрированый обход L
#     if node:
#         print_range(node.left, left, right)
#         if right >= node.value >= left:
#             print(node.value)
#         print_range(node.right, left, right)


def print_range(node, left, right):
    if node:


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8


test()
