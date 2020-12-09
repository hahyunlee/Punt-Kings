from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from src.data import pipeline
import pandas as pd
import numpy as np


def _predict_cat(X_train, y_train, X_test, y_test, X_final):

    lr = LinearRegression()
    lasso = Lasso(alpha=0.5)
    ridge = Ridge(alpha=0.5)

    lr.fit(X_train,y_train)
    lasso.fit(X_train,y_train)
    ridge.fit(X_train,y_train)

    y_pred = _find_best_model(X_final,X_test,y_test, y_train,lr,lasso,ridge)

    return y_pred



def _find_best_model(X_final,X_test, y_test, model_1, model_2, model_3):
    """
    This method will compare the train/test results and find the best RMSE of 4 models:
        1) LinearRegressions
        2) Ridge
        3) Lasso

    """
    y_pred_1 = model_1.predict(X_test)
    y_pred_2 = model_2.predict(X_test)
    y_pred_3 = model_3.predict(X_test)

    rmse_1 = np.sqrt(mean_squared_error(y_test, y_pred_1))
    rmse_2 = np.sqrt(mean_squared_error(y_test, y_pred_2))
    rmse_3 = np.sqrt(mean_squared_error(y_test, y_pred_3))

    list_of_results = [rmse_1,rmse_2,rmse_3]

    # Find the best the best model based on prediction and y_test
    if rmse_1 == min(list_of_results):
        y_final = model_1.predict(X_final)
    elif rmse_2 == min(list_of_results):
        y_final = model_2.predict(X_final)
    else:
        y_final = model_3.predict(X_final)

    return y_final


def predict_all_cats(dict_dfs, list_cats, latest_season = 'df_2019', final_season = 'df_2020'):
    X_final = pipeline.prepare_final_data(dict_dfs[final_season])
    df = pd.DataFrame()
    df['Player'] = dict_dfs[latest_season].Player

    for cat in list_cats:
        X,y = pipeline.prepare_all_data(dict_dfs,cat,latest_season)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

        y_prediction = _predict_cat(X_train, y_train, X_test, y_test, X_final)

        df[cat] = y_prediction.round(3)

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