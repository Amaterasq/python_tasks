'''
Дана матрица.
Нужно написать функцию, которая для элемента
возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего
на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Формат ввода:
В первой строке задано n — количество строк матрицы.
Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица.
Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента,
соседей которого нужно найти.
Индексация начинается с нуля.

Формат вывода:
Напечатайте нужные числа в возрастающем порядке через пробел.
'''


# n, m = int(input()), int(input())  # число строк и столбцов
# matrix = []
# for _ in range(n):  # ввод матрицы
#     matrix.append(list(map(int, input().split())))
# x, y = int(input()), int(input())  # координаты иск


def neighbours(n, m, matrix, x, y):
    neigh_lst = []
    if x - 1 >= 0:
        neigh_lst.append(matrix[x - 1][y])
    if y - 1 >= 0:
        neigh_lst.append(matrix[x][y - 1])
    if y + 1 < m:
        neigh_lst.append(matrix[x][y + 1])
    if x + 1 < n:
        neigh_lst.append(matrix[x + 1][y])
    return sorted(neigh_lst)


# print(*neighbours(n, m, matrix, x, y))


assert neighbours(
    4, 3,
    [
        [1, 2, 3],
        [0, 2, 6],
        [7, 4, 1],
        [2, 7, 0]
    ],
    3, 0) == [7, 7]


assert neighbours(
    4, 3,
    [
        [1, 2, 3],
        [0, 2, 6],
        [7, 4, 1],
        [2, 7, 0]
    ],
    0, 0) == [0, 2]