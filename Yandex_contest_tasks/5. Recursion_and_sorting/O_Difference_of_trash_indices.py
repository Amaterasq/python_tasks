'''
Гоша долго путешествовал и измерил площадь каждого из n островов
Алгосов, но ему этого мало! Теперь он захотел оценить,
насколько разнообразными являются острова в составе архипелага.

Для этого Гоша рассмотрел все пары островов
(таких пар, напомним, n * (n-1) / 2) и посчитал
попарно разницу площадей между всеми островами.
Теперь он собирается упорядочить полученные разницы,
чтобы взять k-ую по порядку из них.

Помоги Гоше найти k-ю минимальную разницу между площадями
эффективно.

Пояснения к примерам
Пример 1
Выпишем все пары площадей и найдём соответствующие разницы

|2 - 3| = 1
|3 - 4| = 1
|2 - 4| = 2
Так как нам нужна 2-я по величине разница, то ответ будет 1.
Пример 2
У нас есть два одинаковых элемента в массиве —– две единицы,
поэтому минимальная (первая) разница равна нулю.

Формат ввода:
В первой строке записано натуральное число n –— количество
островов в архипелаге (2 ≤ n ≤ 100 000).

В следующей строке через пробел записаны n площадей
островов — n натуральных чисел, каждое из которых
не превосходит 1 000 000.

В последней строке задано число k. Оно находится в
диапазоне от 1 до n(n - 1) / 2.

Формат вывода:
Выведите одно число –— k-ую минимальную разницу.
'''

'''
Рабочее, не проходит по памяти
def dif(amount, list, k):
    dif_list = [None] * (amount * (amount - 1) // 2)
    id = 0
    while list != []:
        num1 = list.pop()
        for num2 in list:
            dif_list[id] = abs(num1-num2)
            id += 1
    dif_list.sort()
    return dif_list[k - 1]


print(dif(int(input()), list(map(int, input().split())), int(input())))
'''


def check_index(array, middle, k_position, s_len):
    left = count = 0
    for right in range(s_len):
        val_right = array[right]
        val_left = array[left]
        while val_right - val_left > middle:
            left += 1
            val_left = array[left]
        count += right - left
        if count >= k_position:
            return True
    return False


def diff(s_len, s, k_position):
    s.sort()
    left, right = 0, s[-1] - s[0]
    while left < right:
        middle = (left + right) // 2
        if check_index(s, middle, k_position, s_len):
            right = middle
        else:
            left = middle + 1
    return left


print(diff(int(input()), list(map(int, input().split())), int(input())))
