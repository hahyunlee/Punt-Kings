from src.data import pipeline
from src.models import predict_model
from pathlib import Path

def _get_project_root() -> Path:
    return Path(__file__).parent.parent

root = str(_get_project_root())
path_avg = '/data/season_avg'
path_tot = '/data/season_totals'

if __name__ == "__main__":
    df_list = pipeline.load_data(root+path_tot)
    df_dict = pipeline.create_df_dict(df_list,first_season=1990)

    # A list of statistical categories we want to project
    list_cats = ['PTS','FG','FGA','3P','3PA','FT','FTA','ORB','DRB',
                 'AST','STL','BLK','TOV','G','GS','MP']

    final_projections_df = predict_model.predict_all_cats(df_dict,list_cats,
                                                          latest_season='df_2019',final_season='df_2020')

    print(final_projections_df)