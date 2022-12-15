'''
Вам будет предоставлен массив чисел.
Вы должны отсортировать нечетные числа в порядке возрастания,
оставив четные числа на их исходных позициях.
'''


def sort_array(source_array):
    even_sort = iter(sorted([i for i in source_array if i % 2 != 0]))
    for cur_id in range(len(source_array)):
        if source_array[cur_id] % 2 != 0:
            source_array[cur_id] = next(even_sort)
    return source_array


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []
