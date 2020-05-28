from EDA import Target, Features
from machine_learning import XGBoost

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

    XGBoost.run_xgboost(preprocessed_df, target)

if __name__ == '__main__':
    main()