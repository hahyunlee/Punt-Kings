


league_id = 0000
draft_results = "https://basketball.fantasysports.yahoo.com/nba/{0}/draftresults".format(league_id)








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