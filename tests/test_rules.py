from app.src.rules import *
import pytest


def test_test_csv_correct_file():
    for i in range(1, 6):
        # every test must have its own Rules instance
        rules = Rules()
        assert rules.test_csv_file('tests/csv/test' + str(i) + '_t.csv') is True


def test_test_csv_wrong_file():
    for i in range(1, 30):
        # every test must have its own Rules instance
        rules = Rules()
        assert rules.test_csv_file('tests/csv/test' + str(i) + '_f.csv') is False


@pytest.mark.parametrize(
    'guess, result, points',
    [
        (None, None, 0),
        (None, ("Group Stage", "Chelsea", "Liverpool", 1, 1, 12, 12, 2000), 0),
        (("Honza420", "Group Stage", "Liverpool", "Chelsea", 1, 1), None, 0),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 1, 1),
         ("Group Stage", "Chelsea", "Liverpool", 1, 1, 12, 12, 2000), 20),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 1, 1),
         ("Group Stage", "Chelsea", "Liverpool", 5, 5, 12, 12, 2000), 5),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 5, 5),
         ("Group Stage", "Chelsea", "Liverpool", 1, 1, 12, 12, 2000), 5),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 6, 0),
         ("Group Stage", "Chelsea", "Liverpool", 1, 1, 12, 12, 2000), 0),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 1, 1),
         ("Group Stage", "Chelsea", "Liverpool", 6, 0, 12, 12, 2000), 0),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 3, 1),
         ("Group Stage", "Chelsea", "Liverpool", 5, 2, 12, 12, 2000), 5),
        (("Honza420", "Group Stage", "Chelsea", "Liverpool", 3, 6),
         ("Group Stage", "Chelsea", "Liverpool", 1, 2, 12, 12, 2000), 5),
        # swapping home team and away team is a different match
        (("Honza420", "Group Stage", "Liverpool", "Chelsea", 3, 1),
         ("Group Stage", "Chelsea", "Liverpool", 1, 3, 12, 12, 2000), 0),
        (("Honza420", "Winner", "Liverpool"),
         ("Final-Full Result", "Chelsea", "Real Madrid", 2, 0, 12, 12, 2000), 0),
        (("Honza420", "Winner", "Liverpool"),
         ("Final-Full Result", "Chelsea", "Liverpool", 2, 0, 12, 12, 2000), 0),
        (("Honza420", "Winner", "Liverpool"),
         ("Final-Full Result", "Chelsea", "Liverpool", 1, 3, 12, 12, 2000), 125)
    ]
)
def test_determine_points(guess, result, points):
    assert determine_points(guess, result) == points
