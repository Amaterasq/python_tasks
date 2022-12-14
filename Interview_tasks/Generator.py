'''
Напишите генератор, который принимает на вход число
и возвращает это число в степени номера итерации до указанного
(до бесконечности по стандарту)
'''


def generator(num):
    power = 1
    while True:
        yield num**power
        power += 1


a = generator(2)  # С каким начальным числом создаем генератор
count_iter = 5    # Сколько раз возвращаем результат по условию

for _ in range(count_iter):
    print(next(a))
