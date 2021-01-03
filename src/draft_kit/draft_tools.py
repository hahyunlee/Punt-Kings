from urllib.request import urlopen
from bs4 import BeautifulSoup


league_id = 0000
draft_results = "https://basketball.fantasysports.yahoo.com/nba/{0}/draftresults".format(league_id)


def _scrape_results(league_id=0000):
    url = "https://basketball.fantasysports.yahoo.com/nba/{0}/draftresults".format(league_id)
    players = []

    html = urlopen(url)
    soup = BeautifulSoup(html)

    for line in soup.find_all('td'):
        if line.a == None:
            continue
        else:
            players.append(line.a.get_text())

    return players



def find_best_available(df,league_id=0000):
    """
    Scrape draft results and store the player names being taken and recorded

    Take out row based on player name

    Every time you run the returning DataFrame provides only names of those available

    :param df:
    :return:
    """

    players_drafted = _scrape_results(league_id)

    filter = df['Player'].isin(players_drafted)
    df = df.loc[~filter].head(50).reset_index(drop=True)

    return df


def calculate_team_stats(df,league_id=0000):

    _scrape_results(league_id)

    return df

