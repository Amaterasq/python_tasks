class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iterable
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for el in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(el):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield el


# class multifilter:
    
#     judge_half = lambda fx: sum(fx) >= len(fx)/2
#     judge_any = lambda fx: any(fx)
#     judge_all = lambda fx: all(fx)

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge

#     def __iter__(self):
#         return (x for x in self.iterable if self.judge([f(x) for f in self.funcs]))



def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]