'''
Задача повышенной сложности
На каждом острове в архипелаге Алгосы живёт какое-то количество
людей или же остров необитаем (тогда на острове живёт 0 людей).
Пусть на i-м острове численность населения составляет ai.
Тимофей захотел найти медиану среди всех значений численности
населения.

Определение: Медиана
(https://ru.wikipedia.org/wiki/Медиана_(статистика))
массива чисел a_i —– это такое число, что половина чисел из
массива не больше него, а другая половина не меньше.
В общем случае медиану массива можно найти, отсортировав
числа и взяв среднее из них. Если количество чисел чётно,
то возьмём в качестве медианы полусумму соседних средних
чисел, (a[n/2] + a[n/2 + 1])/2.

У Тимофея уже есть отдельно данные по северной части
архипелага и по южной, причём значения численности населения
в каждой группе отсортированы по неубыванию.

Определите медианную численность населения по всем островам Алгосов.

Подсказка: Если n –— число островов в северной части архипелага,
а m –— в южной, то ваше решение должно работать за O(log(n+m)).

Формат ввода:
В первой строке записано натуральное число n, во
второй —– натуральное число m. Они не превосходят 10 000.

Далее в строку через пробел записаны n целых неотрицательных чисел,
каждое из которых не превосходит 10 000, –— значения численности
населения в северной части Алгосов.

В последней строке через пробел записаны m целых неотрицательных
чисел, каждое из которых не превосходит 10 000 –— значения
численности населения в южной части Алгосов.

Значения в третьей и четвёртой строках упорядочены по неубыванию.

Формат вывода:
Нужно вывести одной число — найденную медиану.
'''
