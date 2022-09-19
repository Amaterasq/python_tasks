import sqlite3

# Прочитаем и выведем в консоль все поля всех записей из таблицы movies
con = sqlite3.connect('Databases/data.sqlite')
cur = con.cursor()

# Верни все столбцы всех записей из таблицы movies;
# символ * после SELECT означает "верни все поля найденных записей".
# cur.execute('''
#     SELECT *
#     FROM movies;
# ''')

# Получаем конкретные поля
# cur.execute('''
# SELECT name,
#        release_year
# FROM movies;
# ''')

# Фильтрация с помощью WHERE
cur.execute('''
SELECT name,
       release_year
FROM movies
WHERE release_year > 1980;
''')

# Python превращает результирующую выборку в итерируемый объект,
# который можно перебрать циклом:
for result in cur:
    print(result)

# При получении данных из таблицы коммит не нужен.
con.close()
