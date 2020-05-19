import pandas as pd


def feature_engineer(df):
    print(df)

    df['redWins'] = df['blueWins'].apply(lambda x: 1 if x == 0 else 0)

    return df
