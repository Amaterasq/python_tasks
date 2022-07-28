'''
Гоше дали задание написать красивую сортировку слиянием.
Поэтому Гоше обязательно надо реализовать отдельно функцию
merge и функцию merge_sort.
Функция merge принимает два отсортированных массива,
сливает их в один отсортированный массив и возвращает его.
Если требуемая сигнатура имеет вид merge(array, left, mid, right),
то первый массив задаётся полуинтервалом
[left,mid) массива array, а второй – полуинтервалом [mid,right)
массива array.
- Функция merge_sort принимает некоторый подмассив,
  который нужно отсортировать. Подмассив задаётся
  полуинтервалом — его началом и концом.
- Функция должна отсортировать передаваемый в неё подмассив,
  она ничего не возвращает.
- Функция merge_sort разбивает полуинтервал
  на две половинки и рекурсивно вызывает сортировку
  отдельно для каждой. Затем два отсортированных массива
  сливаются в один с помощью merge.
Заметьте, что в функции передаются именно полуинтервалы
[begin,end), то есть правый конец не включается.
Например, если вызвать merge_sort(arr, 0, 4),
где arr=[4,5,3,0,1,2], то будут отсортированы только
первые четыре элемента, изменённый массив будет выглядеть
как arr=[0,3,4,5,1,2].

Реализуйте эти две функции.

Формат ввода:
Передаваемый в функции массив состоит из целых чисел,
не превосходящих по модулю 109. Длина сортируемого диапазона
не превосходит 105.
'''


def merge_sort(arr, lf, rg):
    if lf >= rg:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid + 1, rg)
    merge(arr, lf, mid + 1, rg)


def merge(arr, lf, mid, rg):
    left_sub, right_sub = arr[lf:mid], arr[mid:rg + 1]
    left_sub_id, right_sub_id = 0, 0
    sorted_id = lf

    while left_sub_id < len(left_sub) and right_sub_id < len(right_sub):
        if left_sub[left_sub_id] <= right_sub[right_sub_id]:
            arr[sorted_id] = left_sub[left_sub_id]
            left_sub_id += 1
        else:
            arr[sorted_id] = right_sub[right_sub_id]
            right_sub_id += 1
        sorted_id += 1

    while left_sub_id < len(left_sub):
        arr[sorted_id] = left_sub[left_sub_id]
        left_sub_id += 1
        sorted_id += 1

    while right_sub_id < len(right_sub):
        arr[sorted_id] = right_sub[right_sub_id]
        right_sub_id += 1
        sorted_id += 1
    return arr


'''
def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


test()
'''
