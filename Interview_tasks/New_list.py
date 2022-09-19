'''
Напишите свой класс NewList,
наследующийся от стандартного list.
Переопределите поведение метода так, чтобы
нумерация списка начиналась с 1, а не с 0
'''


class NewList(list):
    '''Мб добавить работу со слайсами'''
    def __getitem__(self, index):
        if index == 0:
            raise IndexError('ListIndexOutOfRange')
        if index >= 1:
            return super().__getitem__(index - 1)
        return super().__getitem__(index)


new_list = NewList([1, 2, 3, 4, 5])
print(new_list[1])

# lst = [1, 2, 3, 4, 5]
# print(lst[1:])
