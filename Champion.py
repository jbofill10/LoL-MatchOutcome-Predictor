import requests
import json
import os
import pprint
import pickle

import numpy as np


def get_champions(ids):
    if not os.path.isfile('Data/pickles/champions'):
        r = requests.get('http://ddragon.leagueoflegends.com/cdn/10.10.3216176/data/en_US/champion.json')

        response = r.json()

        champions_reformatted = {}

        for champion in response['data']:
            id = response['data'][champion]['key']

            champions_reformatted[int(id)] = 'Wukong' if champion == 'MonkeyKing' else champion

        with open('Data/pickles/champions', 'wb') as file:
            pickle.dump(champions_reformatted, file)
    else:
        with open('Data/pickles/champions', 'rb') as file:
            champions_reformatted = pickle.load(file)

    champions = []

    for id in ids:

        champions.append('None' if id == -1 else champions_reformatted[id])

    return champions[0] if len(champions) == 1 else champions


def format_champs(df, cols, head):
    champ_dict = {}

    for col in cols:
        champs = df[col].value_counts()

        champ_names = get_champions(champs.keys())
        freq = [i for i in champs]
        counter = 0
        for name in champ_names:

            champ_dict[name] = champ_dict.setdefault(name, 0) + freq[counter]

            counter += 1

    champ_dict = {k: v for k, v in sorted(champ_dict.items(), key=lambda item: item[1], reverse=True)}

    top_n = dict(list(champ_dict.items())[0:head])

    other = dict(list(champ_dict.items())[head+1:])

    other_total = 0
    top_n_total = 0

    for key, val in top_n.items():
        top_n_total += val

    for key, val in other.items():
        other_total += val

    other_total = np.abs(top_n_total-other_total)

    top_n['Other'] = other_total

    return top_n
