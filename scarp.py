import re
import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.sportinglife.com/football/fixtures-results/competitions/english-fa-cup/76/2022-01"

try:
    html_content = requests.get(url, timeout=4.0).text
except requests.exceptions.RequestException as e:
    print("ERROR network")
    sys.exit(1)

soup = BeautifulSoup(html_content, "html.parser")
dates = soup.findAll('li', class_='DatesList__ListItem-sc-1iq29n-0 bVBqIz')
for date in dates:
    matches = date.findAll('li', class_='List__ItemWrapper-sc-2hb99l-1 ljzDJb')
    for match in matches:
        try:
            match_live_clock = match.find('div', class_='Item__MatchLiveClock-et8305-3 sekoJ').text
            # extra time / penalties
            if match_live_clock == 'AET':
                details_url = 'https://www.sportinglife.com' + match.find('a')['href']
                print("AET: \t\t", details_url)
            elif match_live_clock != 'FT':
                print('--------PASS---------')
                pass
            else:
                score = match.find('span', class_='Item__TeamsModifier-et8305-7 iEeIun').text
                score = re.findall('[0-9]+', score)

            home_team = match.find('span', class_='Item__TeamA-et8305-6 leKmkN').text
            away_team = match.find('span', class_='Item__TeamB-et8305-8 bHURVJ').text
            print(f'{home_team} {score[0]}:{score[1]} {away_team}')
        except Exception as e:
                print("ERROR during scarping")
                sys.exit(2)

