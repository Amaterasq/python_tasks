'''
Дана абстрактная файловая система вида:
├─ dir1
│ └─ dir2
│ ├─ file1
│ └─ file2
└─ dir3
В каждой директории содержится либо файлы,
либо поддиректория (вложенность не ограничена),
либо она может быть пустой.
Требуется написать функцию biggestPath(X: dict) -> str,
принимающую в качестве аргумента словарь X
(описывающий файловую систему) и возвращающую
самый длинный найденный в нем корректный путь в виде строки
(либо строку "/" если такой путь в словаре не найден).
Критерии корректного пути:
- ключ словаря (подсловаря) интерпретировать как имя директории
- значение словаря (подсловаря) интерпретировать как набор
поддиректорий (вложенный словарь) или файлов (вложенный список)
- имена директорий/файлов должны состоят только из букв английского
алфавита и цифр
- длина пути должна быть не более 255 символов
(с учетом знака / , разделяющего компоненты пути)
- в одной папке не могут находится директории/файлы с одинаковыми именами

## Пример 1.
python
[IN]
d1 = {
    'dir1': {},
    'dir2': ['file1'],
    'dir3': {'dir4': ['file2'],
    'dir5': {'dir6': {'dir7': {}}}}
}
[OUT]
/dir3/dir5/dir6/dir7

## Пример 2.
python
[IN]
d2 = {'dir1': ['file1', 'file1']}
[OUT]
/

## Пример 3.
python
[IN]
d3 = {'dir1': ['file1', 'file2', 'file2']}
[OUT]
/dir1/file1
'''


d1 = {
    'dir1': {},
    'dir2': ['file1'],
    'dir3': {
        'dir4': ['file2'],
        'dir5': {'dir6': {'dir7': {}}}
    },
}

d2 = {
    'dir1': [
        'file1',
        'file1'
    ]
}

d3 = {
    'dir1': [
        'file1',
        'file2',
        'file2'
    ]
}

d4 = {
    'dir1': {},
    'dir2': {
        'dir3': {
            'dir4': {
                'dir5': ['a'*250, 'file2']
            }
        }
    },
    'dir6': ['file1', 'file2', 'file3', 'file4']
}

d5 = {
    'dir1': ['a'*255],
}


def biggestPath(obj, path='', paths=None):
    if paths is None:
        paths = []
    if obj == {} or isinstance(obj, str):
        if path in paths:
            paths.remove(path)
        else:
            paths.append(path)
        return path
    elif isinstance(obj, dict):
        for key, value in obj.items():
            biggestPath(value, path + f'/{key}', paths)
    elif isinstance(obj, list):
        for item in obj:
            biggestPath(item, path + f'/{item}', paths)
    try:
        max_path = max(paths, key=lambda x: x.count('/'))
        while len(max_path) > 255:
            paths.remove(max_path)
            max_path = max(paths, key=lambda x: x.count('/'))
        return max_path
    except ValueError:
        return '/'


assert biggestPath(d1) == '/dir3/dir5/dir6/dir7'
assert biggestPath(d2) == '/'
assert biggestPath(d3) == '/dir1/file1'
assert biggestPath(d4) == '/dir2/dir3/dir4/dir5/file2'
assert biggestPath(d5) == '/'
