import pytest
from app.src.util import is_positive_integer


@pytest.mark.parametrize(
    'n, expected',
    [
        (1, True),
        (10000000000000, True),
        (420, True),
        (-1, False),
        (-999999999999999991, False),
        (1.2, False),
        ("dddddddd", False),
        ('a', False)
    ]
)
def test_is_positive_integer(n, expected):
    assert expected == is_positive_integer(n)
