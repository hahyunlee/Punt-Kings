from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

def _get_project_root() -> Path:
    return Path(__file__).parent.parent.parent

root = str(_get_project_root())


# Load season stats from Basketball Reference
def scrape_br(year, averages=True):

    nba_season = year

    if averages:
        url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(nba_season)
    else:
        url =  "https://www.basketball-reference.com/leagues/NBA_{}_totals.html".format(nba_season)

    html = urlopen(url)
    soup = BeautifulSoup(html, features="lxml")

    soup.findAll('tr', limit=2)
    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
    headers = headers[1:]

    rows = soup.findAll('tr')[1:]
    player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

    df = pd.DataFrame(player_stats, columns=headers)

    return df


def bulk_scrape(start_year, end_year = 2019, averages=True):
    for season in range(start_year,end_year+1):
        df = scrape_br(season,averages)
        if averages:
            df.to_csv(root+'/data/season_avg/{}_avg.csv'.format(season))
        else:
            df.to_csv(root + '/data/season_totals/{}_totals.csv'.format(season))
    return


if __name__ == "__main__":
    # Scrape season totals from 1990
    # bulk_scrape(1990,2019,averages=False)
