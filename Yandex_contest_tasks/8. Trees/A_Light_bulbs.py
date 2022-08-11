'''
Гоша повесил на стену гирлянду в виде бинарного дерева,
в узлах которого находятся лампочки. У каждой лампочки есть
своя яркость. Уровень яркости лампочки соответствует числу,
расположенному в узле дерева. Помогите Гоше найти самую яркую
лампочку в гирлянде, то есть такую, у которой яркость наибольшая.

Формат ввода:
На вход подается корень дерева.
Решение нужно отправлять в виде файла с расширением,
которое соответствует вашему языку программирования.
Если вы пишете на Java, имя файла должно быть Solution.java,
для C# – Solution.cs.
Для остальных языков назовите файл my_solution.ext,
заменив ext на необходимое расширение.

Формат вывода:
Функция должна вернуть максимальное значение яркости в узле дерева.
'''


# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def solution(root):
    if root is None:
        return float('-inf')
    res = root.value
    left_res = solution(root.left)
    right_res = solution(root.right)
    if left_res > res:
        res = left_res
    if right_res > res:
        res = right_res
    return res

# def test():
#     node1 = Node(1)
#     node2 = Node(-5)
#     node3 = Node(3, node1, node2)
#     node4 = Node(2, node3, None)
#     assert solution(node4) == 3
