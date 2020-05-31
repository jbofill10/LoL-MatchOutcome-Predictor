import os
import pandas as pd

from riotwatcher import LolWatcher
from dotenv import load_dotenv
from time import sleep

import pprint
import numpy as np


# load_dotenv()


def query_games(game_ids):
    if not os.path.isfile('Data/pickles/riotapi_res_pickle'):

        # Riot games api allows 100 requests per 2 min
        counter = 0

        game_meta_df = pd.DataFrame()
        for gameId in game_ids:

            if counter == 100:
                counter = 0
                sleep(120)

            response = query_game(gameId, 'EUW1')

            game_meta_df = game_meta_df.append(parse_json(response), ignore_index=True)

            counter += 1

        # print(game_meta_df)
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
def query_game(gameId, area):
    watcher = LolWatcher(os.getenv("API_KEY"))
    while True:
        try:
            response = watcher.match.by_id(area, gameId)

        except:
            continue
        break

    return response


# Gets games given encrypted account Id
# Purpose of this was to validate my models aside from train test split
def get_more_games(user):
    pp = pprint.PrettyPrinter(indent=4)
    watcher = LolWatcher(os.getenv("API_KEY"))
    matches = []

    while True:
        try:
            response = watcher.match.matchlist_by_account("NA1", user)
        except Exception as e:
            print(user)
            print(e)
            continue
        break

    for match in response['matches']:
        matches.append(match['gameId'])

    return matches


# Basically creates the original data set I got from kaggle so I can expand my data set beyond 10k games
def game_timeline(game_id):
    pp = pprint.PrettyPrinter(indent=4)
    watcher = LolWatcher(os.getenv("API_KEY"))

    row = {
    }

    blue_wards_placed = 0
    blue_wards_destroyed = 0
    blue_kills = 0
    blue_deaths = 0
    blue_assists = 0
    blue_elite_monsters = 0
    blue_dragons = 0
    blue_heralds = 0
    blue_towers_destroyed = 0
    blue_total_gold = 0
    blue_avg_level = 0
    blue_total_experience = 0
    blue_total_minions = 0
    blue_total_jungle_minions = 0
    blue_gold_diff = 0
    blue_exp_diff = 0
    blue_gold_per_min = 0
    red_wards_placed = 0
    red_wards_destroyed = 0
    red_kills = 0
    red_deaths = 0
    red_assists = 0
    red_elite_monsters = 0
    red_dragons = 0
    red_heralds = 0
    red_towers_destroyed = 0
    red_total_gold = 0
    red_avg_level = 0
    red_total_experience = 0
    red_total_minions = 0
    red_total_jungle_minions = 0
    red_gold_diff = 0
    red_exp_diff = 0
    red_gold_per_min = 0

    blue = [1, 2, 3, 4, 5]
    while True:
        try:
            res = watcher.match.timeline_by_match("NA1", game_id)
        except:
            print("Retrying...")
            continue

        break
    # riot api uses ms for timestamp unit -- so ms to min
    frame_interval = res['frameInterval'] / 60000

    game_clock = 0

    for frame in res['frames']:
        for event in frame['events']:
            if event['type'] == 'WARD_PLACED':
                if event['creatorId'] in blue:
                    blue_wards_placed += 1
                else:
                    red_wards_placed += 1

            if event['type'] == 'WARD_KILL':
                if event['killerId'] in blue: blue_wards_destroyed += 1

                else: red_wards_destroyed += 1

            if event['type'] == 'BUILDING_KILL':
                if 'INHIBITOR' in event['buildingType']:
                    if event['teamId'] == 100: blue_towers_destroyed += 1

                    else: red_towers_destroyed += 1
            if event['type'] == 'ELITE_MONSTER_KILL':
                if 'HERALD' in event['monsterType']:
                    if event['killerId'] in blue: blue_heralds += 1
                    else: red_heralds += 1

                elif event['monsterType'] == 'DRAGON':
                    if event['killerId'] in blue: blue_dragons += 1
                    else: red_dragons += 1

                else:
                    if event['killerId'] in blue: blue_elite_monsters += 1
                    else: red_elite_monsters += 1

            if event['type'] == 'CHAMPION_KILL':
                if event['killerId'] in blue:
                    blue_kills += 1
                    red_deaths += 1
                else:
                    blue_kills += 1
                    red_deaths += 1
                if event["assistingParticipantIds"]:
                    if event['killerId'] in blue:
                        blue_assists += len(event["assistingParticipantIds"])
                    else:
                        red_assists += len(event["assistingParticipantIds"])

        if game_clock >= 11:
            blue_levels = []
            red_levels = []
            for part_frame, part_stats in frame['participantFrames'].items():
                if part_stats['participantId'] in blue:
                    blue_total_gold += part_stats['totalGold']
                    blue_total_experience += part_stats['xp']
                    blue_total_minions += part_stats['minionsKilled']
                    blue_total_jungle_minions += part_stats['jungleMinionsKilled']
                    blue_levels.append(part_stats['level'])
                else:
                    red_total_gold += part_stats['totalGold']
                    red_total_experience += part_stats['xp']
                    red_total_minions += part_stats['minionsKilled']
                    red_total_jungle_minions += part_stats['jungleMinionsKilled']
                    red_levels.append(part_stats['level'])

            blue_avg_level = np.mean(blue_levels)
            red_avg_level = np.mean(red_levels)

            blue_gold_diff = blue_total_gold - red_total_gold
            red_gold_diff = red_total_gold - blue_total_gold

            blue_exp_diff = blue_total_experience - red_total_experience
            red_exp_diff = red_total_experience - blue_total_experience

            blue_gold_per_min = blue_total_gold / 10
            red_gold_per_min = red_total_gold / 10

            break

        game_clock += frame_interval

    row['gameId'] = game_id
    row['blueWardsPlaced'] = blue_wards_placed
    row['blueWardsDestroyed'] = blue_wards_destroyed
    row['blueKills'] = blue_kills
    row['blueDeaths'] = blue_deaths
    row['blueAssists'] = blue_assists
    row['blueEliteMonsters'] = blue_elite_monsters
    row['blueDragons'] = blue_dragons
    row['blueHeralds'] = blue_heralds
    row['blueTowersDestroyed'] = blue_towers_destroyed
    row['blueTotalGold'] = blue_total_gold
    row['blueAvgLevel'] = round(blue_avg_level, 1)
    row['blueTotalExperience'] = blue_total_experience
    row['blueTotalMinionsKilled'] = blue_total_minions
    row['blueTotalJungleMinionsKilled'] = blue_total_jungle_minions
    row['blueGoldDiff'] = blue_gold_diff
    row['blueExperienceDiff'] = blue_exp_diff
    row['blueGoldPerMin'] = round(blue_gold_per_min, 1)

    row['redWardsPlaced'] = red_wards_placed
    row['redWardsDestroyed'] = red_wards_destroyed
    row['redKills'] = red_kills
    row['redDeaths'] = red_deaths
    row['redAssists'] = red_assists
    row['redEliteMonsters'] = red_elite_monsters
    row['redDragons'] = red_dragons
    row['redHeralds'] = red_heralds
    row['redTowersDestroyed'] = red_towers_destroyed
    row['redTotalGold'] = red_total_gold
    row['redAvgLevel'] = round(red_avg_level, 1)
    row['redTotalExperience'] = red_total_experience
    row['redTotalMinionsKilled'] = red_total_minions
    row['redTotalJungleMinionsKilled'] = red_total_jungle_minions
    row['redGoldDiff'] = red_gold_diff
    row['redExperienceDiff'] = red_exp_diff
    row['redGoldPerMin'] = round(red_gold_per_min, 1)

    combined = row
    combined.update(parse_json_v2(query_game(game_id, 'NA1')))

    return combined


def parse_json_v2(response):
    parsed_json = {}

    blue_cs = 0
    red_cs = 0

    blue = [1, 2, 3, 4, 5]

    # Get participants info
    part_count = 1
    for participant in response['participants']:
        if part_count == 6:
            part_count = 1
        team = 'blue' if participant['teamId'] == 100 else 'red'
        parsed_json['{}_champ_{}'.format(team, part_count)] = participant['championId']
        part_count += 1
        if 'creepsPerMinDeltas' in participant['timeline']:
            if participant['timeline']['participantId'] in blue:
                blue_cs += participant['timeline']['creepsPerMinDeltas']['0-10']
            else:
                red_cs += participant['timeline']['creepsPerMinDeltas']['0-10']
        else:
            blue_cs = np.nan
            red_cs = np.nan
    # Get bans and other info from teams
    for team in response['teams']:

        for bans in team['bans']:

            parsed_json['ban_{}'.format(bans['pickTurn'])] = bans['championId']

        curr_team = 'blue' if team['teamId'] == 100 else 'red'

        parsed_json['{}_baronKills'.format(curr_team)] = team['baronKills']
        parsed_json['{}_dragonKills'.format(curr_team)] = team['dragonKills']
        parsed_json['{}_firstBaron'.format(curr_team)] = 1 if team['firstBaron'] else 0
        parsed_json['{}firstBlood'.format(curr_team)] = 1 if team['firstBlood'] else 0
        parsed_json['{}_firstInhibitor'.format(curr_team)] = 1 if team['firstInhibitor'] else 0
        parsed_json['{}_firstRiftHerald'.format(curr_team)] = 1 if team['firstRiftHerald'] else 0
        parsed_json['{}_inhibitorKills'.format(curr_team)] = team['inhibitorKills']
        parsed_json['{}_riftHeraldKills'.format(curr_team)] = team['riftHeraldKills']
        parsed_json['{}_towerKills'.format(curr_team)] = team['towerKills']

        if team['teamId'] == 100:
            parsed_json['blueWins'] = 1 if team['win'] == 'Win' else 0

    parsed_json['blueCSPerMin'] = blue_cs
    parsed_json['redCSPerMin'] = red_cs

    return parsed_json



