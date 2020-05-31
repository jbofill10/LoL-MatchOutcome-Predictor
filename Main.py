from EDA import Target, Features
from machine_learning import XGBoost, LogisticRegression, RandomForest
from sklearn.model_selection import train_test_split

import pandas as pd
import QueryGames
import Preprocessing
import os
import pickle
from time import sleep

from dotenv import load_dotenv

load_dotenv()


def main():
    df = pd.read_csv('Data/high_diamond_ranked_10min.csv')

    game_ids = list(df['gameId'].values)

    meta_df = QueryGames.query_games(game_ids)

    df = pd.concat([df, meta_df], axis=1)
    df.drop(['blue_firstBlood', 'red_firstBlood'], axis=1, inplace=True)

    Features.feature_eda(df)
    
    Target.target_eda(df)

    if not os.path.isfile('Data/pickles/more_gameids'):

        acc_ids = os.getenv("ACCOUNT_IDS").split(" ")
        acc_ids = list(map(str.strip, acc_ids))

        more_game_ids = []
        counter = 0
        print(acc_ids)
        for account in acc_ids:

            if 20 % counter == 0 and counter != 0:
                sleep(120)

            more_game_ids += QueryGames.get_more_games(account)
            counter += 1

            print("Queries to go: {}".format(len(acc_ids) - counter))

        with open('Data/pickles/more_gameids', 'wb') as file:
            pickle.dump(more_game_ids, file)

    else:
        with open('Data/pickles/more_gameids', 'rb') as file:
            more_game_ids = pickle.load(file)

    if not os.path.isfile('Data/pickles/more_games'):
        more_games_df = pd.DataFrame()
        counter = 0
        for i in more_game_ids:
            if counter % 100 == 0 and counter != 0:
                sleep(120)

            more_games_df = more_games_df.append(QueryGames.game_timeline(i), ignore_index=True)

            counter += 1
            print('{} Queries remaining'.format(len(more_game_ids)-counter))

        more_games_df.to_pickle('Data/pickles/more_games')
    else:
        more_games_df = pd.read_pickle('Data/pickles/more_games')

    more_games_df.dropna(inplace=True)
    more_games_df.reset_index(inplace=True)
    more_games_df.rename(columns={"redfirstBlood": 'redFirstBlood', 'bluefirstBlood': 'blueFirstBlood'}, inplace=True)
    more_games_df['redWins'] = more_games_df['blueWins'].apply(
        lambda x: 1 if x == 0 else 0
    )

    more_games_df = more_games_df[df.columns.tolist()]

    combined_df = pd.concat([df, more_games_df], axis=0, ignore_index=True)

    train_df, test_df, train_target, test_target = Preprocessing.preprocess(combined_df, len(df))

    #XGBoost.train(train_df, train_target)
    XGBoost.predict(test_df, test_target)

    #LogisticRegression.train(train_df, train_target)
    LogisticRegression.predict(test_df, test_target)

    #RandomForest.train(train_df, train_target)
    RandomForest.predict(test_df, test_target)


if __name__ == '__main__':
    main()