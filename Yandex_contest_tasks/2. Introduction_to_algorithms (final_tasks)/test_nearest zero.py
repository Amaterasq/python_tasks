import pytest

import A_Nearest_zero


@pytest.mark.parametrize(
    'houses, expected',
    (
        (
            ['0', '1', '4', '9', '0'],
            [0, 1, 2, 1, 0]
        ),
        (
            ['0', '7', '9', '4', '8', '20'],
            [0, 1, 2, 3, 4, 5]
        ),
        (
            [
                '99', '0', '100', '72', '43', '49',
                '0', '51', '19', '61', '93', '31'
            ],
            [1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 4, 5]
        ),
        (
            ['98', '0', '10', '77', '0', '59', '28', '0', '94'],
            [1, 0, 1, 1, 0, 1, 1, 0, 1]
        )
    )
)
def test_nearest_zero(houses, expected):
    assert A_Nearest_zero.dist_for_nearest_zero(houses) == expected
