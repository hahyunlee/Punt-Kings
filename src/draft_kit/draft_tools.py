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


# def best_cats(df, player_name, list_cats):
#     new_df = df[df['Name'] == player_name]
#     new_df = new_df[list_cats].squeeze().sort_values(ascending=False)
#     return new_df
#
#
# def build_team(df, player_name, draft_df=pd.DataFrame(),
#                cats=['Name', 'pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV'], add=True):
#     if add:
#         if draft_df.empty:
#             draft_df = df[df['Name'] == player_name][cats]
#         else:
#             draft_df = pd.concat([draft_df, df[df['Name'] == player_name][cats]], sort=False)
#     else:
#         draft_df = draft_df[draft_df.Name != player_name]
#     return draft_df
#
#
# def find_best_player(df, draft_df, list_names,
#                      keep_cats=['Name', 'pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV']):
#     avg = pd.DataFrame()
#     value = []
#
#     for name in list_names:
#         new_df = build_team(df, name, draft_df, keep_cats)
#         value.append(get_averages(new_df).mean())
#
#     avg['Name'] = list_names
#     avg['Overall'] = value
#     avg.sort_values(['Overall'], ascending=False, inplace=True)
#     return avg