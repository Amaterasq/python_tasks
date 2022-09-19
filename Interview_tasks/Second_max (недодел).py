'''
Найдите второй максимум в массиве за один прохо по массиву
'''


def second_max(array):
    try:
        if array[0] > array[1]:
            max_1, max_2 = array[0], array[1]
        else:
            max_1, max_2 = array[1], array[0]
    except IndexError:
        return None
    index = 2
    while max_1 == max_2:
        if max_1 > array[index]:
            max_2 = array[index]
        elif max_1 < array[index]:
            max_1 = array[index]
        index += 1
    for num in array[2:]:
        if num > max_1:
            max_2, max_1 = max_1, num
        elif num > max_2:
            max_2 = num
    return max_2


def test_second_max():
    result = second_max([3, 2, -10, 2, 100, 45])
    assert result == 45, f'Wrong answer: {result}'
    result = second_max([1])
    assert result is None, f'Wrong answer: {result}'
    result = second_max([])
    assert result is None, f'Wrong answer: {result}'
    result = second_max([100, 100, 99])
    assert result == 99, f'Wrong answer: {result}'
    print('Все тесты пройдены!')


if __name__ == '__main__':
    test_second_max()
