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
