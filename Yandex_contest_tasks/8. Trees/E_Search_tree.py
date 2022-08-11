'''
Гоша понял, что такое дерево поиска, и захотел написать функцию,
которая определяет, является ли заданное дерево деревом поиска.
Значения в левом поддереве должны быть строго меньше,
в правом —- строго больше значения в узле.
Помогите Гоше с реализацией этого алгоритма.

Формат ввода:
На вход функции подается корень бинарного дерева.
Замечания про отправку решений
По умолчанию выбран компилятор make.
Решение нужно отправлять в виде файла с расширением,
которое соответствует вашему языку программирования.
Если вы пишете на Java, имя файла должно быть Solution.java,
для C# – Solution.cs.
Для остальных языков назовите файл my_solution.ext,
заменив ext на необходимое расширение.
'''

'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
'''

'''Пояснение: -inf и inf нужны для избежания ошибок
в случае, если относительно поддерева вершины расположены правильно,
но неправильно относительно корня дерева или более высокой вершины.'''


def solution(node, min=float('-inf'), max=float('inf')):
    if node is None:
        return True
    if node.value <= min or max <= node.value:
        return False
    return (
        solution(node.left, min, node.value)
        and solution(node.right, node.value, max)
    )


'''
def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


test()
'''
