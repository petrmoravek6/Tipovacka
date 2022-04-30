import os
import sqlite3
import sys
from datetime import datetime


class Database:
    def __init__(self):
        self.__connect()
        self.db.execute("""CREATE TABLE if not exists player (
                        nickname_player text NOT NULL PRIMARY KEY,
                        full_name_player text NOT NULL
                        )""")
        self.db.execute("""CREATE TABLE if not exists match_result (
            phase TEXT NOT NULL,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            away_team_score INTEGER NOT NULL,
            home_team_score INTEGER NOT NULL,
            date_day INTEGER NOT NULL,
            date_month INTEGER NOT NULL,
            date_year INTEGER NOT NULL,
            PRIMARY KEY (phase, home_team, away_team)
        );""")
        self.db.execute("""CREATE TABLE if not exists match_guess_gs (
            nickname_player TEXT NOT NULL,
            phase TEXT NOT NULL,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            away_team_score INTEGER NOT NULL,
            home_team_score INTEGER NOT NULL,
            PRIMARY KEY (nickname_player, phase, home_team, away_team)
        );""")
        self.db.execute("""CREATE TABLE if not exists match_guess_ks (
                    nickname_player TEXT NOT NULL,
                    phase TEXT NOT NULL,
                    team TEXT NOT NULL,
                    PRIMARY KEY (nickname_player, phase, team)
                );""")
        self.__commit_and_close()

    def __connect(self):
        self.conn = sqlite3.connect('database.db')
        self.db = self.conn.cursor()

    def __commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def player_exists(self, nickname):
        self.__connect()
        self.db.execute("SELECT * FROM player WHERE nickname_player=?", (nickname,))
        if self.db.fetchone() is None:
            self.__commit_and_close()
            return False
        else:
            self.__commit_and_close()
            return True

    def add_player(self, nickname, name):
        self.__connect()
        self.db.execute("INSERT INTO player VALUES (?, ?)", (nickname, name))
        self.__commit_and_close()

    def del_player(self, nickname):
        self.__connect()
        self.db.execute("DELETE FROM player WHERE nickname_player=?", (nickname,))
        self.db.execute("DELETE FROM match_guess WHERE nickname_player=?", (nickname,))
        self.__commit_and_close()

    def add_match_guess_gs(self, name, phase, home_team, away_team, home_team_score, away_team_score):
        self.__connect()
        self.db.execute("INSERT INTO match_guess VALUES (?,?,?,?,?,?)",
                        (name, phase, home_team, away_team, home_team_score, away_team_score))
        self.__commit_and_close()

    def add_match_guess_ks(self, name, phase, team):
        self.__connect()
        self.db.execute("INSERT INTO match_guess VALUES (?,?,?)",
                        (name, phase, team))
        self.__commit_and_close()

    def add_match_result(self, phase, home_team, away_team, home_team_score, away_team_score, day, month, year):
        self.__connect()
        self.db.execute("INSERT OR IGNORE INTO match_result VALUES (?,?,?,?,?,?,?,?)",
                        (phase, home_team, away_team, home_team_score, away_team_score, day, month, year))
        self.__commit_and_close()

    def get_date_of_last_result(self):
        self.__connect()
        self.db.execute(
            "SELECT date_day, date_month, date_year FROM match_result ORDER BY date_year DESC, date_month DESC, date_day DESC ")
        date = self.db.fetchone()
        self.__commit_and_close()
        if date is None:
            return None
        return datetime(date[2], date[1], date[0])

    def print_all_playes(self):
        self.__connect()
        self.db.execute(
            "SELECT * FROM player")
        print(self.db.fetchall())
        self.__commit_and_close()

    def print_all_guesses(self):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_guess")
        print(self.db.fetchall())
        self.__commit_and_close()

    def print_all_results(self):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_result")
        print(self.db.fetchall())
        self.__commit_and_close()
