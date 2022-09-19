
'''
Интересный случай, разобраться почему так
a = (i**2 for i in range(1, 5))
print(type(a))  # <class 'generator'>
# print(next(a))
for i in a:
    print(i)
'''

# b = [i**2 for i in range(1, 5)]
# print(type(b))  # <class 'list'>
