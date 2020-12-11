import glob
import pandas as pd
import numpy as np


def load_data(path,file_type='csv'):
    data_files = glob.glob(path + "/*."+file_type)
    data_files = sorted(data_files)
    df_list = []

    for file_ in data_files:
        if file_type == 'xls':
            df = pd.read_excel(file_, index_col=None, header=0)
            df_list.append(df)
        elif file_type == 'csv':
            df = pd.read_csv(file_, index_col=None, header=0)
            df_list.append(df)
        else:
            error_log = "Method currently only reads xls or csv files."
            return error_log
    return df_list


def create_df_dict(df_list,first_season=1990):
    df_dict = {}
    df_names = []
    columns = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG',
               'FGA', '3P', '3PA', '2P', '2PA', 'eFG%', 'FT',
               'FTA', 'ORB', 'DRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

    for year in range(first_season,first_season+len(df_list)):
        df_names.append(year)

    for df, name in zip(df_list, df_names):
        df_dict['df_{0}'.format(name)] = df[columns]
        # Clean DataFrame and store into dictionary
        df_dict['df_{0}'.format(name)] = _clean_br_df(df_dict['df_{0}'.format(name)])

    return df_dict


def _clean_br_df(df):
    """
    This method will clean our raw data by dropping empty rows, refining player positions to 5 major positions,
    removing players playing for multiple teams (aggregate rows), and dummify player positions.

    :param df:
    :return:
    """

    # Take out empty rows
    df.dropna(how='all',inplace=True)

    # Convert multiple positions to a primary position from Basketball Reference
    df['Pos'] = df['Pos'].apply(lambda s: s[:2])
    df['Pos'].mask(df['Pos']=='C-', 'C', inplace=True)

    # Take out the rows for the player that played in multiple teams and keep their TOT stats
    multi_teams_player_list = (df.loc[(df['Tm']=='TOT')].Player).tolist()
    mask_1 = df['Player'].isin(multi_teams_player_list)
    mask_2 = df['Tm']!="TOT"
    df = df.loc[~( (mask_1) & (mask_2) )]

    # Remove team column
    df.drop(columns=['Tm'],inplace=True)

    # Replace NaN eFG% w/ 0
    df['eFG%'].mask(df['eFG%'].isna(),0,inplace=True)

    # Dummify player positions
    df = pd.get_dummies(df, columns=['Pos'])


    # Use only baseline features:
    # baseline_features = ['Player','G','FG','FGA','FT','FTA','3P', '3PA',
    #                  'ORB', 'DRB', 'AST', 'STL', 'BLK', 'TOV','PTS']
    # df = df[baseline_features]

    return df


def _prepare_data(df_old, df_new, target_colname):
    """
    This method will merge dataframes from the preceding season, joined by player name.
    The later season will be our target variables based on last season performance and we will train
    our data from previous 30+ seasons.

    X will be our training data, and y will be one statistical variable we will predict.
    Will be recursively called to predict

    Ex:
    X,y = prepare_data(df_2018, df_2019, 'PTS')

    Will grab points from the new season and attach to a dataframe from the previous season where PTS_y is
    the new target. X will be the values from the previous season and y being the target stat.

    :return: X values, and target y
    """

    df_new = df_new.filter(items=['Player', target_colname])
    df = df_old.merge(df_new, left_on='Player', right_on='Player', how='inner')
    y = df[target_colname + '_y']
    X = df.drop(columns=['Player', target_colname+ '_y']).values

    return X, y

def prepare_all_data(dict_dfs, target_colname, newest_year = "df_2019"):
    """
    We ultimately want to predict the new season based on the previous season.
    The most recent season completed will be our X data we will use for the best model we find.
    This means we exclude the most recent season for training/cross-validating.

    :param dict_dfs:
    :param target_colname:
    :param newest_year:
    :return: combined X and y for all seasons in the dictionary
    """

    # Get the index of the newest year in the dictionary of dfs
    last_idx = sorted(dict_dfs.keys()).index(newest_year)

    # Creating 2 list of keys, one with all keys, another without the earliest season key
    keys_1 = sorted(dict_dfs.keys())
    keys_2 = sorted(dict_dfs.keys())[1:last_idx + 1]

    # Create a list of X variables and y target corresponding to  every season
    list_X = []
    list_y = []

    # Recursively calling prepare_data method for a season and the season following, storing X, y in lists
    for i, j in zip(keys_1, keys_2):
        X, y = _prepare_data(dict_dfs[i], dict_dfs[j], target_colname)
        list_X.append(X)
        list_y.append(y)

    # Creating/combining all the necessary components for modeling
    X = np.concatenate(list_X)
    y = np.concatenate(list_y)

    return X, y


# Preparing test variables (for the most recent season)
def prepare_final_data(df):
    """
    This should be the most recent completed season used for predicting newest season.

    :param df:
    :return:
    """
    X_final = df.drop(columns=['Player']).values
    return X_final


def project_baseline_model_result(df,target_stat):
    """

    If we find that replicating our target from last season as our projection is the best result,
    we will use last year's results as our projection as well.

    """
    y_target = df[target_stat]

    return y_target

