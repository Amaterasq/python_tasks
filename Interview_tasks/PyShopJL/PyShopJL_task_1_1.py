from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 100

PROBABILITY_SCORE_CHANGED = 0.1

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offsets": [0],
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
        "offsets": [previous_value["offsets"][-1] + offset_change],
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp_i = generate_stamp(current_stamp)
        if current_stamp_i['score'] == current_stamp['score']:
            current_stamp['offsets'].append(current_stamp_i['offsets'][0])
        else:
            stamps.append(current_stamp_i)
            current_stamp = current_stamp_i
    return stamps


game_stamps = generate_game()

pprint(game_stamps)


# Решение
def get_score(game_stamps, offset):
    home, away = next(
        (d.get('score').get('home'), d.get('score').get('away'))
        for d in game_stamps if offset in d.get('offsets')
    )
    return home, away


# print(get_score(game_stamps, 0))
