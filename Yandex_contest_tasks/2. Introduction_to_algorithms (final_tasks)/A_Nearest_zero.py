'''
Тимофей ищет место, чтобы построить себе дом.
Улица, на которой он хочет жить, имеет длину n,
то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей
на этой улице. Поэтому ему важно для каждого участка знать
расстояние до ближайшего пустого участка.
Если участок пустой, эта величина будет равна
нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния.
Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке,
в котором строились, поэтому их номера на карте
никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106).
В следующей строке записаны n целых неотрицательных
чисел — номера домов и обозначения пустых участков на карте (нули).
Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля.
Числа выводите в одну строку, разделяя их пробелами.
'''

'''
def dist_for_nearest_zero(houses, const='0'):  # без векторизации
    result = [0] * len(houses)
    zero_ids = [
        zero_id for zero_id, value in enumerate(houses)
        if value == const
    ]
    first_zero, last_zero = zero_ids[0], zero_ids[-1]
    for number in range(0, first_zero):
        result[number] = first_zero - number
    for number in range(last_zero + 1, len(result)):
        result[number] = number - last_zero
    for number in range(len(zero_ids) - 1):
        prev, next = zero_ids[number], zero_ids[number + 1]
        for index in range(prev, next):
            result[index] = min(index - prev, next - index)
    return result
'''


def dist_for_nearest_zero(houses, const='0'):  # с векторизацией
    result = [0] * len(houses)
    zero_ids = [
        zero_id for zero_id, value in enumerate(houses)
        if value == const
    ]
    first, last = zero_ids[0], zero_ids[-1]
    result[:first] = [first - pos for pos in range(first)]
    result[last:] = [pos - last for pos in range(last, len(result))]
    for prev, next in zip(zero_ids, zero_ids[1:]):
        for index in range(prev + 1, next):
            result[index] = min(index - prev, next - index)
    return result


if __name__ == '__main__':
    input()
    print(*dist_for_nearest_zero(input().split(' ')))
