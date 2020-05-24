import requests
import json
import os
import pprint
import pickle


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

        champions.append(champions_reformatted[id])

    return champions
