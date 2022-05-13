# This is as same class as Game in app.src
# The only difference is that it keeps its data in a special file made for testing (argument in constructor)
import sqlite3
from datetime import datetime


class Database:
    def __init__(self, database_filepath):
        self.database_filepath = database_filepath
        self.__connect()
        self.db.execute("""CREATE TABLE if not exists player (
                        nickname_player text NOT NULL PRIMARY KEY,
                        full_name_player text NOT NULL
                        )""")
        self.db.execute("""CREATE TABLE if not exists match_result (
            phase TEXT NOT NULL,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            home_team_score INTEGER NOT NULL,
            away_team_score INTEGER NOT NULL,
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
            home_team_score INTEGER NOT NULL,
            away_team_score INTEGER NOT NULL,
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
        self.conn = sqlite3.connect(self.database_filepath)
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
        self.db.execute("DELETE FROM match_guess_gs WHERE nickname_player=?", (nickname,))
        self.db.execute("DELETE FROM match_guess_ks WHERE nickname_player=?", (nickname,))
        self.__commit_and_close()

    def add_match_guess_gs(self, name, phase, home_team, away_team, home_team_score, away_team_score):
        self.__connect()
        self.db.execute("INSERT INTO match_guess_gs VALUES (?,?,?,?,?,?)",
                        (name, phase, home_team, away_team, home_team_score, away_team_score))
        self.__commit_and_close()

    def add_match_guess_ks(self, name, phase, team):
        self.__connect()
        self.db.execute("INSERT INTO match_guess_ks VALUES (?,?,?)",
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
            "SELECT date_day, date_month, date_year FROM match_result "
            "ORDER BY date_year DESC, date_month DESC, date_day DESC")
        date = self.db.fetchone()
        self.__commit_and_close()
        if date is None:
            return None
        return datetime(date[2], date[1], date[0])

    def get_all_players(self):
        self.__connect()
        self.db.execute(
            "SELECT * FROM player")
        players = self.db.fetchall()
        self.__commit_and_close()
        return players

    def get_all_results(self):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_result")
        results = self.db.fetchall()
        self.__commit_and_close()
        return results

    def get_all_results_ordered_by_date(self):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_result ORDER BY date_year, date_month, date_day")
        results = self.db.fetchall()
        self.__commit_and_close()
        return results

    def get_match_guess_gs(self, nickname_player, phase, home_team, away_team):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_guess_gs WHERE nickname_player=? AND phase=? AND home_team=? AND away_team=?",
            (nickname_player, phase, home_team, away_team))
        guess = self.db.fetchone()
        self.__commit_and_close()
        return guess

    def get_match_guess_ks(self, nickname_player, phase, team):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_guess_ks WHERE nickname_player=? AND phase=? AND team=?",
            (nickname_player, phase, team))
        guess = self.db.fetchone()
        self.__commit_and_close()
        return guess

    def get_all_match_guesses(self, nickname):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_guess_gs WHERE nickname_player=?", (nickname,))
        guesses_gs = self.db.fetchall()
        self.db.execute(
            "SELECT * FROM match_guess_ks WHERE nickname_player=?", (nickname,))
        guesses_ks = self.db.fetchall()
        self.__commit_and_close()
        return guesses_gs + guesses_ks

    def get_match_result(self, phase, home_t, away_t):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_result WHERE phase=? AND home_team=? AND away_team=?",
            (phase, home_t, away_t))
        res = self.db.fetchone()
        self.__commit_and_close()
        return res

    def get_match_result_by_phase_and_home_team(self, phase, home_t):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_result WHERE phase=? AND home_team=?",
            (phase, home_t))
        res = self.db.fetchone()
        self.__commit_and_close()
        return res

    def get_match_result_by_phase_and_away_team(self, phase, away_t):
        self.__connect()
        self.db.execute(
            "SELECT * FROM match_result WHERE phase=? AND away_team=?",
            (phase, away_t))
        res = self.db.fetchone()
        self.__commit_and_close()
        return res
