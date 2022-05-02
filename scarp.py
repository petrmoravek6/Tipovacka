import csv
import datetime
import re
import sys
import requests
from bs4 import BeautifulSoup


class Scarper:
    request_timeout = 3.0

    def __init__(self, url, competition_start, competition_end):
        self.url = url
        self.competition_start = competition_start
        self.competition_end = competition_end

    def update_results_in_database(self, database):
        most_recent_match_date = database.get_date_of_last_result()
        if most_recent_match_date is None:
            from_date = self.competition_start
        else:
            from_date = max(most_recent_match_date, self.competition_start)
        to_date = min(datetime.datetime.now(), self.competition_end)
        m1 = from_date.month
        y1 = from_date.year
        while (y1, m1) <= (to_date.year, to_date.month):
            self.update_results_in_database_of_month_and_year(database, m1, y1)
            if m1 + 1 == 13:
                m1 = 1
                y1 += 1
            else:
                m1 += 1

    def update_results_in_database_of_month_and_year(self, database, month, year):
        try:
            html_content = requests.get(self.url + '/' + str(year) + '-' + str(str(month).zfill(2)), timeout=Scarper.request_timeout).text
        except requests.exceptions.RequestException:
            print("ERROR network")
            sys.exit(1)
        soup = BeautifulSoup(html_content, "html.parser")
        dates = soup.findAll('li', class_='DatesList__ListItem-sc-1iq29n-0 bVBqIz')
        for date in dates:
            matches = date.findAll('li', class_='List__ItemWrapper-sc-2hb99l-1 ljzDJb')
            date_time = date.find('h3').text + ' ' + str(year)
            datetime_object = datetime.datetime.strptime(date_time, "%A %B %d %Y")
            today = datetime.datetime.now()
            if datetime_object > today:
                break
            for match in matches:
                phase = date.find('h4', class_='RoundList__RoundHeader-sc-718t01-0 dJPQKF')
                if phase is None:
                    phase = "Group Stage"
                else:
                    phase = phase.text
                match_live_clock = match.find('div', class_='Item__MatchLiveClock-et8305-3 sekoJ')
                # The match (at least the standard full time) is not finished yet
                if match_live_clock is None:
                    continue
                match_live_clock = match_live_clock.text
                #scarp final and add it to sql match result database as phase: Final-Full Result
                # extra time / penalties
                if match_live_clock == 'AET':
                    details_url = 'https://www.sportinglife.com' + match.find('a')['href']
                    html_content2 = requests.get(details_url, timeout=4.0).text
                    soup2 = BeautifulSoup(html_content2, "html.parser")
                    time_info = soup2.find('span',
                                           class_='PeriodScores__StyledPeriodScores-sc-6qgbsu-0 cCYRhW').text
                    scores = re.findall('[0-9]+-[0-9]', time_info)
                    score = re.findall('[0-9]+', scores[1])
                    print('AET ', end='')
                    # FT means Full Time. If the match clock isn't FT nor AET then don't scarp anything
                elif match_live_clock == 'FT':
                    score = match.find('span', class_='Item__TeamsModifier-et8305-7 iEeIun').text
                    score = re.findall('[0-9]+', score)
                    # Unknown match_live_clock
                else:
                    continue

                home_team = match.find('span', class_='Item__TeamA-et8305-6 leKmkN').text
                away_team = match.find('span', class_='Item__TeamB-et8305-8 bHURVJ').text
                print(f'{phase}: {home_team} {score[0]}:{score[1]} {away_team},\t{datetime_object}')
                database.add_match_result(phase, home_team, away_team, score[0], score[1], datetime_object.day,
                                          datetime_object.month, datetime_object.year)
