from src.data import pipeline
from src.models import predict_model, projections
from pathlib import Path
import pandas as pd

def _get_project_root() -> Path:
    return Path(__file__).parent.parent

root = str(_get_project_root())
path_avg = '/data/season_avg'
path_tot = '/data/season_totals'
results_path = '/data/projections'
rookies = '/data/projections/rookie_avg.xlsx'


if __name__ == "__main__":
    df_list = pipeline.load_data(root+path_tot)
    df_dict = pipeline.create_df_dict(df_list,first_season=1990)

    df_avg_rookies = pd.read_excel(root+rookies,index_col=0)

    # A list of statistical categories we want to project
    list_cats = ['PTS','FG','FGA','3P','3PA','FT','FTA','ORB','DRB',
                 'AST','STL','BLK','TOV','G','GS','MP']

    final_proj_df = predict_model.predict_all_cats(df_dict,list_cats,
                                                          latest_season='df_2019',final_season='df_2020')

    injured_players = ['Stephen Curry', 'Kyrie Irving', 'Kevin Durant']

    final_proj_df = projections.replace_injured_players(df_dict,final_proj_df,injured_players,2020)

    final_avg_df = projections.create_avg_projections(final_proj_df, df_avg_rookies)

    # Export final projections to excel
    final_proj_df.to_excel(root+results_path+"/final_projections.xlsx")
    final_avg_df.to_excel(root+results_path+"/final_averages.xlsx")
