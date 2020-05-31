from scipy.stats import skew, kurtosis

import pandas as pd

from sklearn.preprocessing import RobustScaler

from sklearn.decomposition import PCA

from prince import MCA

import Champion

import numpy as np


def preprocess(df, train_length):
    df.drop(['redFirstBlood', 'red_firstInhibitor', 'red_firstBaron', 'red_firstRiftHerald', 'gameId'], axis=1,
            inplace=True)

    champ_cols = ['blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
                  'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5', 'ban_1',
                  'ban_2', 'ban_3', 'ban_4', 'ban_5', 'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']

    train_target = df['blueWins'].iloc[:train_length].reset_index(drop=True)
    test_target = df['blueWins'].iloc[train_length:].reset_index(drop=True)

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

    train_df = df.iloc[:train_length].reset_index(drop=True)
    test_df = df.iloc[train_length:, :].reset_index(drop=True)

    train_df_for_scale = train_df[train_df.columns[~train_df.columns.isin(champ_cols)]]

    scaler = RobustScaler()
    scaled_data = scaler.fit_transform(train_df_for_scale)
    pca = PCA(.95)
    pcs = pca.fit_transform(scaled_data)

    train_pca_df = pd.DataFrame(pcs, columns=['PC_{}'.format(i) for i in range(np.size(pcs, 1))])

    champ_df = train_df[train_df.columns[train_df.columns.isin(champ_cols)]]
    champ_select_df = champ_df[champ_cols[:10]]
    champ_ban_df = champ_df[champ_cols[10:]]

    mca_ban = MCA(n_components=5)
    mca_select = MCA(n_components=3)

    ban_mca = mca_ban.fit_transform(champ_ban_df)
    select_mca = mca_select.fit_transform(champ_select_df)

    ban_mca.columns = ['MCA_Ban_{}'.format(i) for i in range(np.size(ban_mca, 1))]
    select_mca.columns = ['MCA_Select_{}'.format(i) for i in range(np.size(select_mca, 1))]

    train_reduced_df = pd.concat([ban_mca, select_mca, train_pca_df], axis=1)

    test_df_for_scale = test_df[test_df.columns[~test_df.columns.isin(champ_cols)]]

    scaled_data = scaler.transform(test_df_for_scale)

    pcs = pca.transform(scaled_data)

    test_pca_df = pd.DataFrame(pcs, columns=['PC_{}'.format(i) for i in range(np.size(pcs, 1))])

    champ_df = test_df[test_df.columns[test_df.columns.isin(champ_cols)]]
    champ_select_df = champ_df[champ_cols[:10]]
    champ_ban_df = champ_df[champ_cols[10:]]

    ban_mca = mca_ban.fit_transform(champ_ban_df)
    select_mca = mca_select.fit_transform(champ_select_df)

    ban_mca.columns = ['MCA_Ban_{}'.format(i) for i in range(np.size(ban_mca, 1))]
    select_mca.columns = ['MCA_Select_{}'.format(i) for i in range(np.size(select_mca, 1))]

    test_reduced_df = pd.concat([ban_mca, select_mca, test_pca_df], axis=1)

    return train_reduced_df, test_reduced_df, train_target, test_target


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


