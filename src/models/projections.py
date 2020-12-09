import pandas as pd

# def replace_neg(df,list_of_cats):
#     new_df = pd.DataFrame()
#     new_df['Name'] = df.Name
#     new_df[list_of_cats] = df[list_of_cats].clip_lower(0)
#     return new_df
#
#
# def calculate_std(df,list_of_cats,totals=True):
#     for colname in list_of_cats:
#         if totals or colname == 'fg%' or colname == 'ft%':
#             if colname == 'to':
#                 df[colname+'V'] = -(df[colname] - df[colname].mean())/df[colname].std()
#             else:
#                 df[colname+'V'] = (df[colname] - df[colname].mean())/df[colname].std()
#         else:
#             if colname == 'to':
#                 df[colname+'V'] = -(df[colname+'/g'] - df[colname+'/g'].mean())/df[colname+'/g'].std()
#             else:
#                 df[colname+'V'] = (df[colname+'/g'] - df[colname+'/g'].mean())/df[colname+'/g'].std()
#     return df
#
#
# def drop_stdvals(df, totals = True):
#     if totals:
#         df.drop(columns = ['fgaV','ftaV'],inplace=True)
#     else:
#         df.drop(columns = ['fga/gV','fta/gV'],inplace=True)
#     return df
#
#
# def calculate_val(df, list_of_cats):
#     df['Value'] = df[list_of_cats].mean(axis=1)
#     return df
#
#
# def punt_cat(df, list_to_punt, list_of_val_cats=['pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV']):
#     diff_list = list(set(list_of_val_cats) - set(list_to_punt))
#     df = calculate_val(df, diff_list)
#     df_all = df.sort_values('Value', ascending=False).reset_index().rename(index=str, columns={'index': 'Orig Rank'})
#     df_all['Orig Rank'] = df_all['Orig Rank'] + 1
#     df_g = df_all[df_all['Pos'] == 'G'].sort_values('Value', ascending=False).reset_index().drop(
#         columns=['Pos', 'index'])
#     df_f = df_all[df_all['Pos'] == 'F'].sort_values('Value', ascending=False).reset_index().drop(
#         columns=['Pos', 'index'])
#     df_c = df_all[df_all['Pos'] == 'C'].sort_values('Value', ascending=False).reset_index().drop(
#         columns=['Pos', 'index'])
#     return df_all, df_g, df_f, df_c
#
#
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
# def get_averages(df):
#     return df.describe().iloc[1].sort_values(ascending=False)
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
#
#
# def replace_player_stats(projected_df, lastlast_season, players):
#     list_df = []
#     list_cats = ['p/g', '3/g', 'r/g', 'a/g', 's/g', 'b/g', 'fg%', 'fga/g', 'ft%', 'fta/g', 'to/g']
#     list_cats2 = ['Name', 'p/g', '3/g', 'r/g', 'a/g', 's/g', 'b/g', 'fg%', 'fga/g', 'ft%', 'fta/g', 'to/g']
#     for name in players:
#         list_df.append(lastlast_season[lastlast_season.Name == name][list_cats2])
#     df = pd.concat(list_df, axis=0)
#     for name in players:
#         df['Name'].replace(name, name + '1', inplace=True)
#     new_df = pd.concat([projected_df, df])
#     for name in players:
#         new_df = new_df[new_df.Name != name]
#         new_df['Name'].replace(name + '1', name, inplace=True)
#     return new_df