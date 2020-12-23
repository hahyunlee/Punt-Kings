import pandas as pd


def create_avg_projections(df, df_rookies):

    df_final_avg = pd.DataFrame()

    df_final_avg['Player'] = df['Player']
    df_final_avg['fg%'] = df['FG'] / df['FGA']
    df_final_avg['fg'] = df['FG']/df['G']
    df_final_avg['fga'] = df['FGA']/df['G']
    df_final_avg['ft%'] = df['FT'] / df['FTA']
    df_final_avg['ft'] = df['FT']/df['G']
    df_final_avg['fta'] = df['FTA']/df['G']
    df_final_avg['3pm'] = df['3P']/df['G']
    df_final_avg['ppg'] = df['PTS']/df['G']
    df_final_avg['rpg'] = (df['ORB']+df['DRB'])/df['G']
    df_final_avg['apg'] = df['AST']/df['G']
    df_final_avg['spg'] = df['STL']/df['G']
    df_final_avg['bpg'] = df['BLK']/df['G']
    df_final_avg['tog'] = df['TOV']/df['G']

    df_final_avg = _add_rookie_projections(df_final_avg, df_rookies).round(2)

    return df_final_avg


def _add_rookie_projections(df_rookies, projections_df):

    list_df = [projections_df,df_rookies]
    projections_df = pd.concat(list_df)

    return projections_df


def _calculate_total_value(df):
    df_final = df.copy()
    value_cols = []

    for col in df_final.columns:
        if col.endswith('_Z'):
            value_cols.append(col)

    df_final['Total'] = df_final[value_cols].sum(axis=1)
    df_final = df_final.sort_values('Total', ascending=False).reset_index(drop=True)

    return df_final


def replace_injured_players(df_dict, projections_df, list_players, injured_year=2020):
    pre_injury = injured_year-1
    df_name = "df_"+str(pre_injury)

    projected_cats = ['Player', 'PTS', 'FG', 'FGA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB',
                      'AST', 'STL', 'BLK', 'TOV', 'G', 'GS', 'MP']
    df_past = df_dict[df_name]

    for player in list_players:
        inj_player = df_past.loc[df_past.Player == player]
        inj_player = inj_player[projected_cats]

        if player in list(projections_df.Player):
            projections_df.loc[projections_df['Player']==player] = inj_player.values
        else:
            projections_df = projections_df.append(inj_player)

    return projections_df


def calculate_zscores(df):
    punt_cats = ['fg%','ft%','3pm','ppg','rpg','apg','spg','bpg','tog']

    for col in punt_cats:
        z_score = (df[col]-df[col].mean()) / df[col].std()
        if col == 'tog':
            df[col+'_V'] = -1 * z_score.round(2)
        elif col!='tog':
            df[col + '_V'] = z_score.round(2)
        else:
            pass

    return df


def punt_cats(df,punt_list=['tog']):
    df_final = df.copy()
    for cat in punt_list:
        df_final.drop(columns=[cat,cat+'_Z'],inplace=True)

    df_final = _calculate_total_value(df_final)

    return df_final

