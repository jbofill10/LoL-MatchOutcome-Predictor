from EDA import Target, Features

import pandas as pd
import QueryGames
import FeatureEngineering


def main():
    df = pd.read_csv('Data/high_diamond_ranked_10min.csv')

    game_ids = list(df['gameId'].values)

    meta_df = QueryGames.query_games(game_ids)

    df = pd.concat([df, meta_df], axis=1)

    df = FeatureEngineering.feature_engineer(df)

    Features.feature_eda(df)
    
    #Target.target_eda(df)

if __name__ == '__main__':
    main()