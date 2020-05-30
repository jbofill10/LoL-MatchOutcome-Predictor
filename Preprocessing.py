from scipy.stats import skew, kurtosis

import pandas as pd

from sklearn.preprocessing import RobustScaler

from sklearn.decomposition import PCA

from prince import MCA

import Champion

import numpy as np


def preprocess(df):
    df.drop(['redFirstBlood', 'red_firstInhibitor', 'red_firstBaron', 'red_firstRiftHerald', 'gameId'], axis=1,
            inplace=True)

    champ_cols = ['blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                  'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                  'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']

    target = df['blueWins']

    df.drop(['blueWins', 'redWins'], axis=1, inplace=True)

    for col in champ_cols:
        df[col] = Champion.get_champions(list(df[col].values))

    removal_list = set()

    for champ_col in champ_cols:

        for key, value in df[champ_col].value_counts(ascending=False).to_dict().items():
            if value < 80:
                for i in range(10):
                    removal_list.add('ban_{}_{}'.format(i, key))
                for i in range(5):
                    removal_list.add('blue_champ_{}_{}'.format(i, key))
                    removal_list.add('red_champ_{}_{}'.format(i, key))

    numerical_cols = [i for i in df if df[i].dtype in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']]
    
    #evaluate_dist(df, numerical_cols)

    cols_to_be_transformed = ['blueWardsDestroyed', 'redWardsDestroyed',
                              'blueWardsPlaced', 'redWardsPlaced',
                              'redTowersDestroyed', 'blueTowersDestroyed']
    
    for col in cols_to_be_transformed:
        df[col] = np.log1p(df[col])
        
    #evaluate_dist(df, cols_to_be_transformed)

    df_for_scale = df[df.columns[~df.columns.isin(champ_cols)]]

    scaler = RobustScaler()
    scaled_data = scaler.fit_transform(df_for_scale)
    pca = PCA(.95)
    pcs = pca.fit_transform(scaled_data)

    pca_df = pd.DataFrame(pcs, columns=['PC_{}'.format(i) for i in range(np.size(pcs, 1))])

    champ_df = df[df.columns[df.columns.isin(champ_cols)]]
    champ_select_df = champ_df[champ_cols[:10]]
    champ_ban_df = champ_df[champ_cols[11:]]

    mca_ban = MCA(n_components=5)
    mca_select = MCA(n_components=3)

    ban_mca = mca_ban.fit_transform(champ_ban_df)
    select_mca = mca_select.fit_transform(champ_select_df)

    ban_mca.columns = ['MCA_Ban_{}'.format(i) for i in range(np.size(ban_mca, 1))]
    select_mca.columns = ['MCA_Select_{}'.format(i) for i in range(np.size(select_mca, 1))]

    reduced_df = pd.concat([ban_mca, select_mca, pca_df], axis=1)

    print(reduced_df)

    return reduced_df, target


def evaluate_dist(df, cols):
    champ_cols = ['blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                  'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                  'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']
    kurtosis_results = dict()
    skewness = dict()

    for i in cols:
        if i not in champ_cols:
            kurtosis_results[i] = kurtosis(df[i])
            skewness[i] = skew(df[i])
    
    kurtosis_results = {k: v for k, v in sorted(kurtosis_results.items(), key=lambda item: item[1])}
    skewness = {k: v for k, v in sorted(skewness.items(), key=lambda item: item[1])}

    print('Skewness:\n')
    [print("{}: {}".format(i, skewness[i])) for i in skewness]

    print('\nKurtosis:\n')
    [print("{}: {}".format(i, kurtosis_results[i])) for i in kurtosis_results]

    print("\n\n")
