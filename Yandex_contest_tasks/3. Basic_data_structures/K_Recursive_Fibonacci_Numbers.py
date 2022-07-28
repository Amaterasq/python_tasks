'''
У Тимофея было n (0≤n≤32) стажёров.
Каждый стажёр хотел быть лучше своих предшественников, поэтому
i-й стажёр делал столько коммитов,
сколько делали два предыдущих стажёра в сумме.
Два первых стажёра были менее инициативными,
они сделали по одному коммиту.
Пусть Fi —– число коммитов, сделанных
i-м стажёром (стажёры нумеруются с нуля).
Тогда выполняется следующее: F0=F1=1.
Для всех i≥2  выполнено Fi=Fi-1+Fi-2.
Определите, сколько кода напишет следующий стажёр –— найдите Fn.
Решение должно быть реализовано рекурсивно.

Формат ввода:
На вход подаётся n — целое число в диапазоне от 0 до 32.
Формат вывода:
Нужно вывести Fn.
'''


def fib(n):
    if n in (1, 0):
        return 1
    return fib(n - 1) + fib(n - 2)


# print(fib(int(input())))

assert fib(3) == 3
assert fib(0) == 1
