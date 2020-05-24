import os
import pandas as pd

from riotwatcher import LolWatcher
from dotenv import load_dotenv
from time import sleep

load_dotenv()


def query_games(game_ids):

    if not os.path.isfile('Data/pickles/riotapi_res_pickle'):

        # Riot games api allows 100 requests per 2 min
        counter = 0

        game_meta_df = pd.DataFrame()
        for gameId in game_ids:

            if counter == 100:
                counter = 0
                sleep(120)

            response = query_game(gameId)

            game_meta_df = game_meta_df.append(parse_json(response), ignore_index=True)

            counter += 1

        #print(game_meta_df)
        game_meta_df.to_pickle('Data/pickles/riotapi_res_pickle')
    else:
        game_meta_df = pd.read_pickle('Data/pickles/riotapi_res_pickle')

    return game_meta_df


def parse_json(response):
    parsed_json = {}

    # Get participants info
    part_count = 1
    for participant in response['participants']:
        if part_count == 6:
            part_count = 1
        team = 'blue' if participant['teamId'] == 100 else 'red'
        parsed_json['{}_champ_{}'.format(team, part_count)] = participant['championId']
        part_count += 1

    # Get bans and other info from teams
    for team in response['teams']:

        for bans in team['bans']:
            parsed_json['ban_{}'.format(bans['pickTurn'])] = bans['championId']

        curr_team = 'blue' if team['teamId'] == 100 else 'red'

        parsed_json['{}_baronKills'.format(curr_team)] = team['baronKills']
        parsed_json['{}_dragonKills'.format(curr_team)] = team['dragonKills']
        parsed_json['{}_firstBaron'.format(curr_team)] = 1 if team['firstBaron'] else 0
        parsed_json['{}_firstBlood'.format(curr_team)] = 1 if team['firstBlood'] else 0
        parsed_json['{}_firstInhibitor'.format(curr_team)] = 1 if team['firstInhibitor'] else 0
        parsed_json['{}_firstRiftHerald'.format(curr_team)] = 1 if team['firstRiftHerald'] else 0
        parsed_json['{}_inhibitorKills'.format(curr_team)] = team['inhibitorKills']
        parsed_json['{}_riftHeraldKills'.format(curr_team)] = team['riftHeraldKills']
        parsed_json['{}_towerKills'.format(curr_team)] = team['towerKills']

    return parsed_json

# Repetitively poll riot games (sorry riot)
# A random 504 error would occur sometimes, this is to prevent that.
def query_game(gameId):
    watcher = LolWatcher(os.getenv("API_KEY"))
    while True:
        try:
            response = watcher.match.by_id('EUW1', gameId)
        except:
            continue
        break

    return response
