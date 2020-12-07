from src.data import pipeline
from pathlib import Path

def _get_project_root() -> Path:
    return Path(__file__).parent.parent

root = str(_get_project_root())
data_path_avg = '/data/season_avg'

if __name__ == "__main__":
    # list_dfs = pipeline._load_data(root + data_path_avg)
    # test_1920 = list_dfs[-1]
    # test_1920['Pos'] = pipeline._convert_positions(test_1920['Pos'])
    #
