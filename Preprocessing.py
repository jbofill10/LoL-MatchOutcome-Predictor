from scipy.stats import skew

import pandas as pd


def feature_engineer(df):
    skewness = dict()
    numerical_cols = [i for i in df if df[i].dtype in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']]

    for i in numerical_cols:
        if i not in ['gameId', 'blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                     'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                     'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']:
            skewness[i] = skew(df[i])

    skewness = {k: v for k, v in sorted(skewness.items(), key=lambda item: item[1])}

    [print("{}: {}".format(i, skewness[i])) for i in skewness]

    return df
