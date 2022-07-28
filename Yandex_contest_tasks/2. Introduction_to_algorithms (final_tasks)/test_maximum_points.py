import pytest

import B_Maximum_points


@pytest.mark.parametrize(
    'k, all_buttons, expected',
    (
        (
            3,
            '12312..22..22..2',
            2
        ),
        (
            4,
            '1111999911119911',
            1
        ),
        (
            4,
            '1111111111111111',
            0
        )
    )
)
def test_maximum_points(k, all_buttons, expected):
    assert B_Maximum_points.maximum_points(k, all_buttons) == expected
