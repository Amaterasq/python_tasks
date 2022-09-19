import sqlite3

con = sqlite3.connect('Databases/data.sqlite')

cur = con.cursor()

# Добавлять записи можно поштучно, вызывая метод execute()
# и передавая в него команду INSERT с нужными данными
# cur.execute('''
#     INSERT INTO movies(id, name, type, release_year)
#     VALUES (1, 'Весёлые мелодии', 'Мультсериал', 1930);
# ''')

# А можно передать в метод execute() значения полей в виде кортежа
# cur.execute('''
#     INSERT INTO movies VALUES (?, ?, ?, ?),
#     (1, 'Весёлые мелодии', 'Мультсериал', 1930)
# ''')

# Или через шорткат - executemany()
directors = [
    (1, 'Текс Эйвери', 1908),
    (2, 'Роберт Земекис', 1952),
    (3, 'Джерри Чиникей', 1912),
]
movies = [
    (1, 'Весёлые мелодии', 'Мультсериал', 1930),
    (2, 'Кто подставил кролика Роджера', 'Фильм', 1988),
    (3, 'Безумные Мелодии Луни Тюнз', 'Мультсериал', 1931),
    (4, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969),
]

cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
cur.executemany('INSERT INTO movies VALUES(?, ?, ?, ?);', movies)

con.commit()
con.close()
