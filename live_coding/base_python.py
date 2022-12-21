a = 'Hello World'
# b = 'Hello World!'
b = a + 'abc'
a = 'Hello Worldabc'
print(a is b, a == b)


# a = [1, 2, 3]
# b = a
# for i in range(len(b)):
#     b[i] += 1
# print(a)
# print(b)


# b = a[:]
# a.append(4)
# b += [4]
# print(a)
# print(b)


# a = list()
# for i in range(1000):
#     a.append(1)
#     if i % 2 == 0:
#         a.append(2)
# print(a)


# fruits = ['apple', 'orange', 'lemon', 'pineapple', 'pear']
# a = {
#     index: fruit
#     for index, fruit in enumerate(fruits)
#     if fruit.startswith('p')
# }

# print(a)