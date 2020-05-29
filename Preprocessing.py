from scipy.stats import skew

import pandas as pd

from sklearn.preprocessing import RobustScaler

import Champion


def preprocess(df):
    df.drop(['redFirstBlood', 'red_firstInhibitor', 'red_firstBaron', 'red_firstRiftHerald', 'gameId'], axis=1,
            inplace=True)

    champ_cols = ['blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                  'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                  'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']

    target = df['blueWins']

    df.drop('blueWins', axis=1, inplace=True)

    for col in champ_cols:
        df[col] = Champion.get_champions(list(df[col].values))
    removal_list = set()
    for champ_col in champ_cols:

        for key, value in df[champ_col].value_counts(ascending=False).to_dict().items():
            if value < 10:
                for i in range(10):
                    removal_list.add('ban_{}_{}'.format(i, key))
                for i in range(5):
                    removal_list.add('blue_champ_{}_{}'.format(i, key))
                    removal_list.add('red_champ_{}_{}'.format(i, key))

    encoded_df = pd.get_dummies(drop_first=False, columns=champ_cols, data=df)

    print(encoded_df.shape)

    encoded_df = encoded_df[encoded_df.columns[~encoded_df.columns.isin(removal_list)]]

    print(encoded_df.shape)

    df_for_scale = df[df.columns[~df.columns.isin(champ_cols)]]

    scaler = RobustScaler()

    scaled_df = pd.DataFrame(scaler.fit_transform(df_for_scale), columns=df_for_scale.columns)

    for col in scaled_df:
        encoded_df[col] = scaled_df[col]

    return encoded_df, target
