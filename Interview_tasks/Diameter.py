'''
Дан двумерный массив из 2 столбцов и 10 строк.
Первый элемент каждой строки представляет
диаметр внутреней, а второй - диаметр внешней
окружности кольца. Напечатать внешние диаметры
тех колец, площадь которых больше площади
прямоугольика с заданными сторонами, и число
таких колец.
'''

from math import pi


arr = [
    [3, 4],
    [2, 1],  # невозможный вариант
    [1, 4],
    [4, 5],
    [5, 8],
    [1, 3],
    [8, 10],
    [3, 9],
    [4, 7],
    [1, 2],
    [21, 40]
]

# S = π / 4 * (D^2 - d^2) - площадь кольца
# S = π * (R^2 - r^2); R, r = 1/2 диаметра - тоже площадь кольца
# S = a * b - площадь прямоугольника

# объявляем результир массив
result = []
for pair in arr:
    if pair[0] >= pair[1]:
        # тут можно выбросить исключение вместо принта
        # Это если внутр d больше или равен внешнему, так быть не может
        print(f'Ошибка в данных (внутр - {pair[0]}, внешн - {pair[1]})')
    # можно через радиус:
    # elif pi * ((pair[1] / 2)**2 - (pair[0] / 2)**2) > pair[0] * pair[1]:
    elif pi / 4 * (pair[1]**2 - pair[0]**2) > pair[0] * pair[1]:
        # если площадь кольца больше - добавляем в результир массив
        result.append(pair[1])
print(f'Внешние d, соотв. условию: {result}', f'Кол-во колец: {len(result)}')