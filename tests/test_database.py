import datetime
from tests.classes_for_testing.game import Database

# db1.db, db2db are databases that could be normally used in our program
# db1.db consists of results of matches that are over and one player "Petr"
# that should have 325 according to rules of the game (325 was manually calculated)
database1 = Database("tests/databases/db1.db")
# db2.db consists of results of matches that are over and two players "Jakub" and "Michal"
# that should have 375 and 325 points according to rules of the game (manually calculated)
database2 = Database("tests/databases/db2.db")


# in both databases the last result is a match played on 4th of May 2022 and the total number
# of played matches is 124


def test_database_get_all_players():
    assert 1 == len(database1.get_all_players())
    assert 2 == len(database2.get_all_players())
    assert "Petr" == database1.get_all_players()[0][0]
    assert "Jakub" == database2.get_all_players()[0][0]
    assert "Michal" == database2.get_all_players()[1][0]


def test_player_exists():
    assert database1.player_exists("Petr") is True
    assert database2.player_exists("Petr") is False
    assert database2.player_exists("Jakub") is True
    assert database2.player_exists("Michal") is True


def test_get_date_of_last_result():
    date = datetime.datetime(2022, 5, 4)
    assert database1.get_date_of_last_result() == date
    assert database2.get_date_of_last_result() == date


def test_results():
    assert len(database1.get_all_results()) == 124
    assert len(database1.get_all_results()) == 124
