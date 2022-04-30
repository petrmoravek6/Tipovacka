import csv


def is_positive_integer(number):
    try:
        val = int(number)
        if val < 0:
            return False
    except ValueError:
        return False
    return True


class Rules:
    def __init__(self):
        self.group_stage_teams_cnt = 96
        self.round_of_16_teams_cnt = 16
        self.quarter_finals_teams_cnt = 8
        self.semi_finals_teams_cnt = 4
        self.final_teams_cnt = 2
        self.winner_cnt = 1
        self.round_of_16_teams = set()
        self.quarter_finals_teams = set()
        self.semi_finals_teams = set()
        self.final_teams = set()
        with open('csv/group_stage_matches.csv', mode='r') as gs_matches_file:
            csv_reader = csv.reader(gs_matches_file)
            self.group_stage_matches = {(row[0], row[1]): False for row in csv_reader}
        with open('csv/list_of_teams.csv', mode='r') as teams_file:
            csv_reader = csv.reader(teams_file)
            self.list_of_teams = {row[0] for row in csv_reader}

    def test_csv_file(self, file):
        with open(file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[0] == 'Group Stage':
                    if self.group_stage_matches.get((row[1], row[2])) != False or not is_positive_integer(row[3]) \
                            or not is_positive_integer(row[4]) or self.group_stage_teams_cnt <= 0:
                        return False
                    self.group_stage_matches[(row[1], row[2])] = True
                    self.group_stage_teams_cnt -= 1
                elif row[0] == 'Round of 16':
                    if row[1] not in self.list_of_teams or self.round_of_16_teams_cnt <= 0 \
                            or row[1] in self.round_of_16_teams:
                        print("8")
                        return False
                    self.round_of_16_teams_cnt -= 1
                    self.round_of_16_teams.add(row[1])
                elif row[0] == 'Quarter-Finals':
                    if row[1] not in self.round_of_16_teams or self.quarter_finals_teams_cnt <= 0 \
                            or row[1] in self.quarter_finals_teams:
                        print("4")
                        return False
                    self.quarter_finals_teams_cnt -= 1
                    self.quarter_finals_teams.add(row[1])
                elif row[0] == 'Semi-Finals':
                    if row[1] not in self.quarter_finals_teams or self.semi_finals_teams_cnt <= 0 \
                            or row[1] in self.semi_finals_teams:
                        print("2")
                        return False
                    self.semi_finals_teams_cnt -= 1
                    self.semi_finals_teams.add(row[1])
                elif row[0] == 'Final':
                    if row[1] not in self.semi_finals_teams or self.final_teams_cnt <= 0 or row[1] in self.final_teams:
                        print("F")
                        return False
                    self.final_teams_cnt -= 1
                    self.final_teams.add(row[1])
                elif row[0] == 'Winner':
                    if row[1] not in self.final_teams or self.winner_cnt <= 0:
                        print("W")
                        return False
                    self.winner_cnt -= 1
                else:
                    print("else")
                    return False
            if self.group_stage_teams_cnt != 0 or self.round_of_16_teams_cnt != 0 \
                    or self.quarter_finals_teams_cnt != 0 or self.semi_finals_teams_cnt != 0 \
                    or self.final_teams_cnt != 0 or self.winner_cnt != 0:
                print("cnt")
                return False
        return True

