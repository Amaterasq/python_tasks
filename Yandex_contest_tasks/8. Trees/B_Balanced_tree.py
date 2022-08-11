'''
Гоше очень понравилось слушать рассказ Тимофея про деревья.
Особенно часть про сбалансированные деревья.
Он решил написать функцию, которая определяет,
сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое
поддеревья каждой вершины отличаются по высоте не больше,
чем на единицу.

Формат ввода:
На вход функции подаётся корень бинарного дерева.

Формат вывода:
Функция должна вернуть True, если дерево сбалансировано
в соответствии с критерием из условия, иначе - False.
'''


'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
'''


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def solution(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if (abs(lh-rh) <= 1) and solution(root.left) and solution(root.right):
        return True
    return False


'''
def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


test()
'''
