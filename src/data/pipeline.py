import glob
import pandas as pd

def _load_xl_ata(path):

    excel_files = glob.glob(path + "/*.xls")
    excel_files = sorted(excel_files)
    files_list = []

    for file_ in excel_files:
        df = pd.read_excel(file_, index_col=None, header=0)
        files_list.append(df)

    return files_list
#
# def _convert_positions_g_f(column):
#
#     for value in column:
#         if value == "PG" or value == "SG" or value == "PG/SG":
#             column = column.replace(value,"G")
#         elif value == "SF" or value == "PF" or value == "SF/PF":
#             column = column.replace(value,"F")
#         else:
#             continue
#
#     return column


#method that converts position to multiple groups after dummifying original table and removing the combined position

def _convert_df_list_to_dict(list_df):
    dict_df = {}
    df_names = ['0304', '0405', '0506', '0607', '0708', '0809', '0910', '1011',
                '1112', '1213', '1314', '1415', '1516', '1617', '1718', '1819', '1920']

    col_names = ['Name', 'Team', 'Pos', 'g', 'm/g', 'p/g', '3/g', 'r/g',
                 'a/g', 's/g', 'b/g', 'fg%', 'fga/g', 'ft%', 'fta/g', 'to/g']

    for df, name in zip(list_df, df_names):
        dict_df['df_{0}'.format(name)] = df[col_names]

    return dict_df


#
# def _run_pipeline(dict_df, season_start, totals=True):
#     season_year = season_start
#     for i in dict_df.keys():
#         dict_df[i] =
#
#     return dict_df
#
# def _merge_previous_season(df,season_year,totals=True):
#     if totals == True:
#         list_cols = ['Round', 'Rank', 'Value', 'Name', 'g', 'm', 'p', '3', 'r', 'a', 's',
#                      'b', 'fg%', 'fga', 'ft%', 'fta', 'to', 'pV', '3V', 'rV', 'aV', 'sV',
#                      'bV', 'fg%V', 'ft%V', 'toV', 'Team_ATL', 'Team_BKN', 'Team_BOS',
#                      'Team_CHA', 'Team_CHI', 'Team_CLE', 'Team_DAL', 'Team_DEN', 'Team_DET',
#                      'Team_FA', 'Team_GSW', 'Team_HOU', 'Team_IND', 'Team_LAC', 'Team_LAL',
#                      'Team_MEM', 'Team_MIA', 'Team_MIL', 'Team_MIN', 'Team_NOR', 'Team_NYK',
#                      'Team_OKC', 'Team_ORL', 'Team_PHI', 'Team_PHO', 'Team_POR', 'Team_SAC',
#                      'Team_SAS', 'Team_SEA', 'Team_TOR', 'Team_UTA', 'Team_WAS', 'Pos_C',
#                      'Pos_F', 'Pos_G']
#     else:
#         list_cols = ['Name', 'g', 'm/g', 'p/g',
#                      '3/g', 'r/g', 'a/g', 's/g', 'b/g', 'fg%', 'fga/g', 'ft%', 'fta/g',
#                      'to/g', 'pV', '3V', 'rV', 'aV', 'sV', 'bV', 'fg%V', 'ft%V', 'toV', 'Team_ATL', 'Team_BKN',
#                      'Team_BOS',
#                      'Team_CHA', 'Team_CHI', 'Team_CLE', 'Team_DAL', 'Team_DEN', 'Team_DET',
#                      'Team_FA', 'Team_GSW', 'Team_HOU', 'Team_IND', 'Team_LAC', 'Team_LAL',
#                      'Team_MEM', 'Team_MIA', 'Team_MIL', 'Team_MIN', 'Team_NOR', 'Team_NYK',
#                      'Team_OKC', 'Team_ORL', 'Team_PHI', 'Team_PHO', 'Team_POR', 'Team_SAC',
#                      'Team_SAS', 'Team_SEA', 'Team_TOR', 'Team_UTA', 'Team_WAS', 'Pos_C',
#                      'Pos_F', 'Pos_G']
#
#
#
# def run_data_pipeline(path):
#     dict_df = _convert_df_list_to_dict(_load_data(path))
#
#     return dict_df

