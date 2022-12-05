# 1 - Поведение изменяемых/неизмеяемых типов данных
# x = 1
# y = 2
# l = [x, y]
# x += 5

# a = [1]
# b = [2]
# s = [a, b]
# a.append(5)

# print(l) # ?
# print(s) # ?


# 2 - Изменяемые аргументы по умолчанию
# def f(x, s=set()):
#     s.add(x)
#     print(s)

# f(7)         # ?
# f(6, {4, 5}) # ?
# f(2)         # ?

# 3 - Замыкания
def f():
    l = [1]
    def inner(x):
        l.append(x)
        return l
    return inner

def g():
    y = 1
    def inner(x):
        y += x
        return y
    return inner

f_inner = f()      # ?
print(f_inner(2))  # ?

g_inner = g()      # ?
print(g_inner(2))  # ?