from EDA import Target, Features
from machine_learning import XGBoost, LogisticRegression, RandomForest
from sklearn.model_selection import train_test_split

import pandas as pd
import QueryGames
import Preprocessing


def main():
    df = pd.read_csv('Data/high_diamond_ranked_10min.csv')

    game_ids = list(df['gameId'].values)

    meta_df = QueryGames.query_games(game_ids)

    df = pd.concat([df, meta_df], axis=1)

    Features.feature_eda(df)
    
    Target.target_eda(df)

    preprocessed_df, target = Preprocessing.preprocess(df)

    x_train, x_test, y_train, y_test = train_test_split(preprocessed_df, target)

    #XGBoost.run_xgboost(x_train, y_train, x_test, y_test)

    #LogisticRegression.run_logit(x_train, y_train, x_test, y_test)
    
    RandomForest.run_rf(x_train, y_train, x_test, y_test)


if __name__ == '__main__':
    main()