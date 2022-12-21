with open('stepik/dataset_24465_4.txt') as inp, open('stepik/copy.txt', 'w') as out:
    data = [line for line in inp.readlines()]
    data.reverse()
    for line in data:
        out.write(line)
