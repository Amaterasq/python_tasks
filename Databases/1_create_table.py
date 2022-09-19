import sqlite3


# Если в текущей директории нет файла db.sqlite -
# он будет создан; сразу же будет создано и соединение с базой.
# Если файл существует, функция connect просто подключится к базе.
con = sqlite3.connect('Databases/data.sqlite')

# Резидентная база создаётся так:
# con = sqlite3.connect(':memory:')

# Создаём специальный объект cursor для работы с БД.
# Вся дальнейшая работа будет вестись через методы этого объекта.
cur = con.cursor()

# Готовим SQL-запросы.
# Для читаемости кода запрос обрамлён в тройные кавычки и разбит построчно.
cur.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    bithday_year INTEGER
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);
''')

# Для одновременного создания нескольких SQL-запросов
# в модуле sqlite3 есть метод executescript()
# cur.executescript('''
# CREATE TABLE IF NOT EXISTS directors(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     bithday_year INTEGER
# );

# CREATE TABLE IF NOT EXISTS movies(
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     type TEXT,
#     release_year INTEGER
# );
# ''')

# Применяем запросы.
# Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# пока не вызван метод commit().
con.commit()

# Закрываем соединение с БД.
con.close()
