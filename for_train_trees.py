
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


# def pre_order(node):  # прямой обход дерева L
#     if node:
#         print(node.value)
#         pre_order(node.left)
#         pre_order(node.right)


# def post_order(node):  # обратный обход дерева L
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value)


def in_order(node):  # центрированый обход L
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)
    # pre_order(node5)
    # post_order(node5)
    in_order(node5)


test()
