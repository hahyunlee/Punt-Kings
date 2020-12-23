from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.data import pipeline
import pandas as pd
import numpy as np


def _predict_cat(X_train, y_train, X_test, y_test, X_final):

    lr = LinearRegression()
    lasso = Lasso(alpha=0.05,max_iter=10000)
    ridge = Ridge(alpha=0.05)

    lr.fit(X_train,y_train)
    lasso.fit(X_train,y_train)
    ridge.fit(X_train,y_train)

    y_pred = _find_best_model(X_final,X_test,y_test,lr,lasso,ridge)

    return y_pred



def _find_best_model(X_final,X_test,y_test, model_1,model_2,model_3):
    """
    This method will compare the train/test results and find the best RMSE of 4 models:
        1) LinearRegressions
        2) Ridge
        3) Lasso

    """
    y_pred_1 = model_1.predict(X_test)
    y_pred_2 = model_2.predict(X_test)
    y_pred_3 = model_3.predict(X_test)

    rmse_1 = np.sqrt(mean_squared_error(y_test, y_pred_1)).round(4)
    rmse_2 = np.sqrt(mean_squared_error(y_test, y_pred_2)).round(4)
    rmse_3 = np.sqrt(mean_squared_error(y_test, y_pred_3)).round(4)

    list_of_results = [rmse_1,rmse_2,rmse_3]

    # Find the best the best model based on prediction and y_test
    if rmse_1 == min(list_of_results):
        y_final = model_1.predict(X_final)
        print('LR model RMSE:',rmse_1)
    elif rmse_2 == min(list_of_results):
        y_final = model_2.predict(X_final)
        print('Lasso model RMSE:',rmse_2)
    else:
        y_final = model_3.predict(X_final)
        print('Ridge model RMSE:',rmse_3)

    return y_final


def _print_baseline_metrics(dict_df, cat, newest_season=2020):
    """
    Here we want to create a baseline model where instead of training data and predicting new results,
    we want to keep the same results from the year prior and set that as our predictions.

    Create our own controlled test set which is the true outcome of the latest season (before the final season),
    and compare the true results from season of 2019 to the season of 2018

    y_test = 2019_season_stats
    y_pred = 2018_season_stats

    :param last_season_stat_col:
    :param y_test:
    :return:
    """
    test_year = newest_season - 1
    train_year = test_year - 1

    df_train = dict_df['df_' + str(train_year)]
    df_test = dict_df['df_' + str(test_year)]

    df = df_train.merge(df_test, left_on='Player', right_on='Player', how='inner')

    y_test = df[cat + '_y'].values
    y_pred = df[cat + '_x'].values

    rmse_base = np.sqrt(mean_squared_error(y_test, y_pred)).round(3)
    print('Baseline model RMSE:', rmse_base)

    return


def predict_all_cats(dict_dfs, list_cats, latest_season = 'df_2019', final_season = 'df_2020'):
    X_final = pipeline.prepare_final_data(dict_dfs[final_season])
    df = pd.DataFrame()
    df['Player'] = dict_dfs[final_season].Player

    for cat in list_cats:
        X,y = pipeline.prepare_all_data(dict_dfs,cat,latest_season)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

        # PRINT METRICS
        print("Predicting:",cat)

        y_final = _predict_cat(X_train, y_train, X_test, y_test, X_final)

        _print_baseline_metrics(dict_dfs,cat,2020)

        df[cat] = y_final.round(3)

    return df





# def r2_scores_cats(dict_of_df,list_of_cats,last_df ='df_1617',test_year = 'df_1718'):
#     for cat in list_of_cats:
#         X_train,y_train = combine_all_data(dict_of_df,cat,last_df)
#         dict_df_test = {k:dict_of_df[k] for k in sorted(dict_of_df.keys())[-2:]}
#         # X_test = prepare_new_data(dict_of_df[last_df])
#         # y_test = dict_of_df[test_year][cat]
#         X_test,y_test = combine_all_data(dict_df_test,cat,test_year)
#         y_pred = predict_cat(X_train,y_train,X_test, model = 'lm')
#         y_avg = np.mean(dict_of_df[last_df][cat])
#         print("R2 Score for ", cat, ": ", r2_score(y_test,y_pred))
#         print("RMSE for ", cat, ": ", np.sqrt(mean_squared_error(y_test, y_pred)))
#         print("RMSE for baseline (average y_test) ", cat, ": ", np.sqrt((1/len(y_pred)) *(np.sum((y_test - y_avg)**2))))