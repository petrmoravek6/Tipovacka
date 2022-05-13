import pytest
from tests.classes_for_testing.game import Game

# db1.db, db2db are databases that could be normally used in our program
# db1.db consists of results of matches that are over and one player "Petr"
# that should have 325 according to rules of the game (325 was manually calculated)
game1 = Game("tests/databases/db1.db")
# db2.db consists of results of matches that are over and two players "Jakub" and "Michal"
# that should have 375 and 325 points according to rules of the game (manually calculated)
game2 = Game("tests/databases/db2.db")


@pytest.mark.parametrize(
    'game, player, points_expected',
    [
        (game1, "Petr", 325),
        (game1, "Honza", 0),
        (game2, "Jakub", 375),
        (game2, "Michal", 325),
        (game2, "sdasdasdasda", 0),
    ]
)
def test_count_points_of_player(game, player, points_expected):
    assert points_expected == game.count_points_of_player(player, game.database.get_all_results())
