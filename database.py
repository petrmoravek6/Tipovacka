import sqlite3


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
            PRIMARY KEY (phase, home_team, away_team)
        );""")
        self.db.execute("""CREATE TABLE if not exists match_guess (
            nickname_player TEXT NOT NULL,
            phase TEXT NOT NULL,
            home_team TEXT NOT NULL,
            away_team TEXT NOT NULL,
            away_team_score INTEGER NOT NULL,
            home_team_score INTEGER NOT NULL,
            PRIMARY KEY (nickname_player, phase, home_team, away_team)
        );""")
        self.conn.commit()
        self.conn.close()

    def __connect(self):
        self.conn = sqlite3.connect('database.db')
        self.db = self.conn.cursor()

    def add_player(self, nickname, name):
        self.__connect()
        self.db.execute("INSERT INTO player VALUES (?, ?)", (nickname, name))
        self.conn.commit()
        self.conn.close()

    def add_match_guess(self, name, phase, home_team, away_team, home_team_score, away_team_score):
        self.__connect()
        self.db.execute("INSERT INTO match_guess VALUES (?,?,?,?,?,?)",
                        (name, phase, home_team, away_team, home_team_score, away_team_score))
        self.conn.commit()
        self.conn.close()

    def select_test(self):
        self.__connect()
        self.db.execute("SELECT * FROM player")
        print(self.db.fetchall())
        self.db.execute("SELECT * FROM match_guess")
        print(self.db.fetchall())
        self.conn.commit()
        self.conn.close()


db = Database()
db.add_player('Honza', 'F K')
db.add_player('Petr', 'F G')
db.add_player('Břéťa', 'R T')
db.add_match_guess('Honza', 'GS', 'Italy', 'Germany', 2, 1)
db.add_match_guess('Petr', 'GS', 'Italy', 'Germany', 2, 1)
db.add_match_guess('Honza', 'GS', 'Sweden', 'Germany', 2, 1)
db.add_match_guess('Honza', 'FI', 'Italy', 'Germany', 2, 1)
db.select_test()
# db.execute("INSERT OR IGNORE INTO match_guess VALUES ('Honza', 'GS', 'Italy', 'Germany', 2, 5)")
# db.execute("INSERT OR IGNORE INTO match_guess VALUES ('Petr', 'GS', 'Italy', 'Germany', 2, 1)")
# db.execute("INSERT OR IGNORE INTO match_guess VALUES ('Honza', 'GS', 'Belgium', 'Germany', 2, 1)")
# db.execute("INSERT OR IGNORE INTO match_guess VALUES ('Honza', 'GS', 'Italy', 'Belgium', 2, 1)")
#
# db.execute("SELECT * FROM match_guess WHERE home_team= 'Belgium'")
# print(db.fetchall())
#
# conn.commit()
# conn.close()
