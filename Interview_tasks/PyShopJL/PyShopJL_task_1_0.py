'''
В примере кода ниже генерируется список фиксаций
состояния счета игры в течение матча.
Разработайте функцию get_score(game_stamps, offset),
которая вернет счет на момент offset в
списке game_stamps.
Нужно суметь понять суть написанного кода,
заметить нюансы, разработать функцию вписывающуюся
стилем в существующий код, желательно адекватной
алгоритмической сложности.
'''


from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 100  # 50000

PROBABILITY_SCORE_CHANGED = 0.1  # 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


# Решение
def get_score(game_stamps, offset):
    try:
        home, away = next(
            (d.get('score').get('home'), d.get('score').get('away'))
            for d in game_stamps if d.get('offset') == offset
        )
    except StopIteration:
        return 'Данный offset не найден'
    return home, away


# Можно сгруппировать данные о матчах
# (т.к. с данными конст результат будет меняться нечасто)
# и искать по вхождению offset в списке offsets
# (если результаты матча не изменяются, добавляем полученный
# offset в список)
# Можно пойти дальше и хранить только две крайние точки.
# Выдавать результат по вхождению заданного offset в отрезок offsets,
# но тут нужно уточнять условия (т.к. будем получать результат
# на как бы несуществующий offset)
# Результат (с немного измененным исходным кодом)
# в файле PyShopJL_testing_2.py


if __name__ == '__main__':
    game_stamps = generate_game()
    pprint(game_stamps)
    print(get_score(game_stamps, 0))
