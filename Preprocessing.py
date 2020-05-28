from scipy.stats import skew

import pandas as pd

from sklearn.preprocessing import RobustScaler

import Champion


def preprocess(df):
    df.drop(['redFirstBlood', 'red_firstInhibitor', 'red_firstBaron', 'red_firstRiftHerald', 'gameId'],  axis=1, inplace=True)

    champ_cols = ['blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                     'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                     'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']

    target = df['blueWins']

    df.drop('blueWins', axis=1, inplace=True)

    for col in champ_cols:
        df[col] = Champion.get_champions(list(df[col].values))

    encoded_df = pd.get_dummies(drop_first=False, columns=champ_cols, data=df)

    df_for_scale = df[df.columns[~df.columns.isin(champ_cols)]]

    scaler = RobustScaler()

    scaled_df = pd.DataFrame(scaler.fit_transform(df_for_scale), columns=df_for_scale.columns)

    for col in scaled_df:
        encoded_df[col] = scaled_df[col]

    '''skewness = dict()
    numerical_cols = [i for i in df if df[i].dtype in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']]

    for i in numerical_cols:
        if i not in ['gameId', 'blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                     'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                     'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']:
            skewness[i] = skew(df[i])

    skewness = {k: v for k, v in sorted(skewness.items(), key=lambda item: item[1])}

    [print("{}: {}".format(i, skewness[i])) for i in skewness]'''

    return encoded_df, target
