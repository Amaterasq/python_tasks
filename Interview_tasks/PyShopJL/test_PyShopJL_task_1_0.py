import unittest
from PyShopJL_task_1_0 import get_score


class TestGetScore(unittest.TestCase):
    def setUp(self):
        self.game_stamps = [
            {'offset': 0, 'score': {'away': 1, 'home': 2}},
            {'offset': 1, 'score': {}},
        ]

    def test_zero_offset(self):
        self.assertEqual(get_score(self.game_stamps, 0), (2, 1))

    def test_non_existent_offset(self):
        self.assertEqual(
            get_score(self.game_stamps, -1),
            'Данный offset не найден'
        )

    def test_non_existent_score(self):
        self.assertEqual(get_score(self.game_stamps, 1), (None, None))


if __name__ == "__main__":
    unittest.main()
