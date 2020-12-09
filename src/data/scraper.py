from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

def _get_project_root() -> Path:
    return Path(__file__).parent.parent.parent

root = str(_get_project_root())

# Load season stats from Basketball Reference
def scrape_br(year, totals=True):

    nba_season = year

    if totals:
        url = "https://www.basketball-reference.com/leagues/NBA_{}_totals.html".format(nba_season)
        file_name = root + '/data/season_totals/{}_totals.csv'.format(nba_season)
    else:
        url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(nba_season)
        file_name = root + '/data/season_avg/{}_avg.csv'.format(nba_season)

    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")

    soup.findAll('tr', limit=2)
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    headers = headers[1:]

    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

    df = pd.DataFrame(player_stats, columns=headers)
    df.to_csv(file_name)

    return


def bulk_scrape(start_year, end_year = 2019, totals=True):
    for season in range(start_year,end_year+1):
        scrape_br(season,totals)
    return


if __name__ == "__main__":
    print('hello')
    # Scrape season totals from 1990 to latest season
    # bulk_scrape(1990,2020,totals=False)
    # Scrape season averages from 1990 to latest season
    # bulk_scrape(1990,2020,totals=True)
