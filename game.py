import csv
import os
import sys
from datetime import datetime
import requests
from database import Database
from rules import Rules
from scarp import Scarper

COMPETITION_URL = "https://www.sportinglife.com/football/fixtures-results/competitions/champions-league/63"
COMPETITION_START = datetime(2021, 9, 14)
COMPETITION_END = datetime(2022, 5, 28)


class Game:
    def __init__(self):
        self.database = Database()
        self.scarper = Scarper(COMPETITION_URL, COMPETITION_START, COMPETITION_END)
        self.update_results()

    def update_results(self):
        try:
            self.scarper.update_results_in_database(self.database)
        except requests.exceptions.RequestException:
            print("ERROR network")
            sys.exit(1)
        except AttributeError:
            print("ERROR during scarping")
            sys.exit(1)

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


class NicknameAlreadyInDatabase(Exception):
    pass


class BadCSVFile(Exception):
    pass
