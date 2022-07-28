'''
Рита решила оставить у себя одежду только трёх цветов:
розового, жёлтого и малинового. После того как вещи других
расцветок были убраны, Рита захотела отсортировать свой новый
гардероб по цветам. Сначала должны идти вещи розового цвета,
потом —– жёлтого, и в конце —– малинового. Помогите Рите
справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода:
В первой строке задано количество предметов в
гардеробе: n –— оно не превосходит 1000000.
Во второй строке даётся массив, в котором указан цвет
для каждого предмета.
Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.

Формат вывода:
Нужно вывести в строку через пробел цвета предметов в правильном порядке.
'''


# Первый вариант
# def sort_clothes(len, arr, count_clothes=3):
#     count_colors = [arr.count(i) for i in range(count_clothes)]
#     index = 0
#     for num_color in range(count_clothes):
#         for _ in range(count_colors[num_color]):
#             arr[index] = num_color
#             index += 1
#     return arr


def sort_clothes(len, arr, count_clohtes=3):  # решение за 1 проход - подсчетом
    count_colors = {str(x): 0 for x in range(count_clohtes)}
    if len > 0:
        for color in arr:
            count_colors[color] += 1
    res = ''.join(
        [key * value for key, value in count_colors.items()]
    ).replace(' ', '')
    return res


# print(*sort_clothes(
#     int(input()),
#     input().split(' ')
# ))


assert sort_clothes(7, '0212001') == '0001122'
assert sort_clothes(5, '21201') == '01122'
assert sort_clothes(6, '211202') == '011222'
