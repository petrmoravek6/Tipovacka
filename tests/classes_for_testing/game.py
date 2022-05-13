# This is as same class as Game in app.src
# The only difference is that it doesn't have Database from app.src, but Database from tests.classes_for_testing
# It takes a file path to database in its constructor's argument
from datetime import datetime
from tests.classes_for_testing.database import Database
from app.src.rules import *
from app.src.scarp import Scarper

COMPETITION_URL = "https://www.sportinglife.com/football/fixtures-results/competitions/champions-league/63"
COMPETITION_START = datetime(2021, 9, 14)
COMPETITION_END = datetime(2022, 5, 28)


class Game:
    def __init__(self, database_filepath):
        self.database = Database(database_filepath)
        self.scarper = Scarper(COMPETITION_URL, COMPETITION_START, COMPETITION_END, self.database)
        self.update_results()

    def update_results(self):
        self.scarper.update_results_in_database()

    def add_player(self, nickname, name, filepath):
        if self.database.player_exists(nickname):
            raise NicknameAlreadyInDatabase
        rules_tester = Rules()
        if not rules_tester.test_csv_file(filepath):
            raise BadCSVFile
        else:
            self.database.add_player(nickname, name)
            with open(filepath, mode='r') as teams_file:
                csv_reader = csv.reader(teams_file)
                for row in csv_reader:
                    if row[0] == 'Group Stage':
                        self.database.add_match_guess_gs(nickname, 'Group Stage', row[1], row[2], row[3], row[4])
                    else:
                        self.database.add_match_guess_ks(nickname, row[0], row[1])

    def remove_player(self, nickname):
        self.database.del_player(nickname)

    def count_points_of_player(self, player_nickname, results):
        cnt = 0
        for res in results:
            if res[0] == 'Group Stage':
                cnt += determine_points(
                    self.database.get_match_guess_gs(player_nickname, 'Group Stage', res[1], res[2]), res)
            elif res[0] == 'Final':
                cnt += determine_points(self.database.get_match_guess_ks(player_nickname, 'Final', res[1]), res)
                cnt += determine_points(self.database.get_match_guess_ks(player_nickname, 'Final', res[2]), res)
            elif res[0] == 'Final-Full Result':
                guess = self.database.get_match_guess_ks(player_nickname, 'Winner', res[1])
                if guess is None:
                    guess = self.database.get_match_guess_ks(player_nickname, 'Winner', res[2])
                cnt += determine_points(guess, res)
            else:
                cnt += determine_points(self.database.get_match_guess_ks(player_nickname, res[0], res[1]), res)

        return cnt


class NicknameAlreadyInDatabase(Exception):
    pass


class BadCSVFile(Exception):
    pass
