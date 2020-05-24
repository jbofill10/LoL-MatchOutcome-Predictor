from plotly.subplots import make_subplots

import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import Champion


def feature_eda(df):
    df['redWins'] = df['blueWins'].apply(lambda x: 1 if x == 0 else 0)

    blue_win = df[df['blueWins'] == 1]
    red_win = df[df['blueWins'] == 0]

    '''

    Wards Placed

    '''

    fig = go.Figure(data=[
        go.Box(name='Blue Win', y=blue_win['blueWardsPlaced'], boxmean=True),
        go.Box(name='Blue Loss', y=red_win['blueWardsPlaced'], boxmean=True),
        go.Box(name='Red Win', y=red_win['redWardsPlaced'], boxmean=True),
        go.Box(name='Red Loss', y=blue_win['redWardsPlaced'], boxmean=True)
    ])

    fig.update_layout(
        title='Wards Placed Distribution',
        height=800,
        width=1200
    )

    # fig.show()

    '''

    Wards Destroyed

    '''

    fig = go.Figure(data=[
        go.Histogram(name='Blue Win', x=blue_win['blueWardsDestroyed']),
        go.Histogram(name='Blue Loss', x=red_win['blueWardsDestroyed']),
        go.Histogram(name='Red Win', x=red_win['redWardsDestroyed']),
        go.Histogram(name='Red Loss', x=blue_win['redWardsDestroyed'])
    ])

    fig.update_layout(
        title='Wards Destroyed Distribution',
        height=800,
        width=1200
    )

    # fig.show()

    '''
    
    First Bloods
    
    '''

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', x=[0], y=[np.sum(blue_win['blueFirstBlood'])], width=0.5),
        go.Bar(name='Blue Loss', x=[1], y=[np.sum(red_win['blueFirstBlood'])], width=0.5),
        go.Bar(name='Red Win', x=[2], y=[np.sum(red_win['redFirstBlood'])], width=0.5),
        go.Bar(name='Red Loss', x=[3], y=[np.sum(blue_win['redFirstBlood'])], width=0.5)
    ])

    fig.update_layout(
        title='The Importance of First Kills',
        height=800,
        width=1200,
        xaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=True
        ),
    )

    # fig.show()

    '''

    Kills

    '''

    fig = go.Figure(data=[
        go.Histogram(name='Blue Win', x=blue_win['blueKills']),
        go.Histogram(name='Blue Loss', x=red_win['blueKills']),
        go.Histogram(name='Red Win', x=red_win['redKills']),
        go.Histogram(name='Red Loss', x=blue_win['redKills'])
    ])

    fig.update_layout(
        title='Distribution of Team Kills when Winning and Losing',
        height=800,
        width=1200,
    )

    # fig.show()

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', x=[0], y=[np.mean(blue_win['blueKills'])], width=0.5),
        go.Bar(name='Blue Loss', x=[1], y=[np.mean(red_win['blueKills'])], width=0.5),
        go.Bar(name='Red Win', x=[2], y=[np.mean(red_win['redKills'])], width=0.5),
        go.Bar(name='Red Loss', x=[3], y=[np.mean(blue_win['redKills'])], width=0.5)
    ])

    fig.update_layout(
        title='Average Kills of Teams when Winning and Losing',
        height=800,
        width=1200,
        xaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=False,
            title='Team'
        ),
    )

    # fig.show()

    '''

    Deaths

    '''

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', x=[0], y=[np.mean(blue_win['blueDeaths'])], width=0.5),
        go.Bar(name='Blue Loss', x=[1], y=[np.mean(red_win['blueDeaths'])], width=0.5),
        go.Bar(name='Red Win', x=[2], y=[np.mean(red_win['redDeaths'])], width=0.5),
        go.Bar(name='Red Loss', x=[3], y=[np.mean(blue_win['redDeaths'])], width=0.5)
    ])

    fig.update_layout(
        title='Average Deaths of Teams when Winning and Losing',
        height=800,
        width=1200,
        xaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=False,
            title='Team'
        ),
    )
    # fig.show()

    '''
    
    Assists
    
    '''

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', x=[0], y=[np.mean(blue_win['blueAssists'])], width=0.5),
        go.Bar(name='Blue Loss', x=[1], y=[np.mean(red_win['blueAssists'])], width=0.5),
        go.Bar(name='Red Win', x=[2], y=[np.mean(red_win['redAssists'])], width=0.5),
        go.Bar(name='Red Loss', x=[3], y=[np.mean(blue_win['redAssists'])], width=0.5)
    ])

    fig.update_layout(
        title='Average Assists of Teams when Winning and Losing',
        height=800,
        width=1200,
        xaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=True
        ),
    )

    # fig.show()

    '''

    Epic Monsters

    '''

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', y=[0], x=[np.sum(blue_win['blueEliteMonsters'])], width=0.5, orientation='h'),
        go.Bar(name='Blue Loss', y=[1], x=[np.sum(red_win['blueEliteMonsters'])], width=0.5, orientation='h'),
        go.Bar(name='Red Win', y=[2], x=[np.sum(red_win['redEliteMonsters'])], width=0.5, orientation='h'),
        go.Bar(name='Red Loss', y=[3], x=[np.sum(blue_win['redEliteMonsters'])], width=0.5, orientation='h')
    ])

    fig.update_layout(
        title='Epic Monsters Killed',
        height=800,
        width=1200,
        yaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=True
        ),
    )

    # fig.show()

    '''

    Rift Heralds

    '''

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', y=[0], x=[np.mean(blue_win['blueHeralds'])], width=0.5, orientation='h'),
        go.Bar(name='Blue Loss', y=[1], x=[np.mean(red_win['blueHeralds'])], width=0.5, orientation='h'),
        go.Bar(name='Red Win', y=[2], x=[np.mean(red_win['redHeralds'])], width=0.5, orientation='h'),
        go.Bar(name='Red Loss', y=[3], x=[np.mean(blue_win['redHeralds'])], width=0.5, orientation='h')
    ])

    fig.update_layout(
        title='Average Rift Heralds Summoned when Winning and Losing',
        height=800,
        width=1200,
        yaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=True
        ),
    )

    # fig.show()

    '''

    Towers Destroyed

    '''

    fig = go.Figure(data=[
        go.Histogram(name='Blue Win', x=blue_win['blueTowersDestroyed']),
        go.Histogram(name='Blue Loss', x=red_win['blueTowersDestroyed']),
        go.Histogram(name='Red Win', x=red_win['redTowersDestroyed']),
        go.Histogram(name='Red Loss', x=blue_win['redTowersDestroyed'])
    ])

    fig.update_layout(
        title='Distribution of Towers Destroyed when Winning and Losing',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    Gold

    '''

    fig = go.Figure(data=[
        go.Violin(name='Blue Win', y=blue_win['blueTotalGold'], meanline_visible=True),
        go.Violin(name='Blue Loss', y=red_win['blueTotalGold'], meanline_visible=True),
        go.Violin(name='Red Win', y=red_win['redTotalGold'], meanline_visible=True),
        go.Violin(name='Red Loss', y=blue_win['redTotalGold'], meanline_visible=True),
    ])

    fig.update_layout(
        title='Gold on Winning and Losing Teams',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    Champ levels

    '''

    fig = go.Figure(data=[
        go.Histogram(name='Blue Win', x=blue_win['blueAvgLevel']),
        go.Histogram(name='Blue Loss', x=red_win['blueAvgLevel']),
        go.Histogram(name='Red Win', x=red_win['redAvgLevel']),
        go.Histogram(name='Red Loss', x=blue_win['redAvgLevel'])
    ])

    fig.update_layout(
        title='Distribution of Champion Levels when Winning and Losing',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    EXP

    '''

    fig = go.Figure(data=[
        go.Box(name='Blue Win', x=blue_win['blueTotalExperience']),
        go.Box(name='Blue Loss', x=red_win['blueTotalExperience']),
        go.Box(name='Red Win', x=red_win['redTotalExperience']),
        go.Box(name='Red Loss', x=blue_win['redTotalExperience'])
    ])

    fig.update_layout(
        title='Total Experience Distrubtion of Champions',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    Minions Killed

    '''

    fig = go.Figure(data=[
        go.Violin(name='Blue Win', y=blue_win['blueTotalMinionsKilled'], meanline_visible=True),
        go.Violin(name='Blue Loss', y=red_win['blueTotalMinionsKilled'], meanline_visible=True),
        go.Violin(name='Red Win', y=red_win['redTotalMinionsKilled'], meanline_visible=True),
        go.Violin(name='Red Loss', y=blue_win['redTotalMinionsKilled'], meanline_visible=True),
    ])

    fig.update_layout(
        title='Minions Killed',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    Jungle Monsters

    '''

    fig = go.Figure(data=[
        go.Violin(name='Blue Win', y=blue_win['blueTotalJungleMinionsKilled'], meanline_visible=True),
        go.Violin(name='Blue Loss', y=red_win['blueTotalJungleMinionsKilled'], meanline_visible=True),
        go.Violin(name='Red Win', y=red_win['redTotalJungleMinionsKilled'], meanline_visible=True),
        go.Violin(name='Red Loss', y=blue_win['redTotalJungleMinionsKilled'], meanline_visible=True),
    ])

    fig.update_layout(
        title='Jungle Monsters Killed',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    CS

    '''

    fig = go.Figure(data=[
        go.Box(name='Blue Win', x=blue_win['blueCSPerMin']),
        go.Box(name='Blue Loss', x=red_win['blueCSPerMin']),
        go.Box(name='Red Win', x=red_win['redCSPerMin']),
        go.Box(name='Red Loss', x=blue_win['redCSPerMin'])
    ])

    fig.update_layout(
        title='CS Per Min Distribution',
        height=800,
        width=1200,
    )

    # fig.show()

    '''

    Bans

    '''

    bans = ['ban_1', 'ban_2', 'ban_3', 'ban_4', 'ban_5',
            'ban_6', 'ban_7', 'ban_8', 'ban_9', 'ban_10']

    for ban in bans:

        fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]],
                            subplot_titles=('Blue {} {}'.format(ban[0:3], ban[4:]),
                                            'Red {} {}'.format(ban[0:3], ban[4:]))
                            )

        row = 1

        blue_win_all_ban = blue_win[ban].value_counts()
        red_win_ban_all_ban = red_win[ban].value_counts()

        blue_win_top_10 = blue_win[ban].value_counts().head(20)
        red_win_top_10 = red_win[ban].value_counts().head(20)

        blue_win_other = np.abs(np.sum(blue_win_top_10) - np.sum(blue_win_all_ban))
        red_win_other = np.abs(np.sum(red_win_top_10) - np.sum(red_win_ban_all_ban))

        blue_vals = blue_win_top_10.values
        red_vals = red_win_top_10.values

        blue_vals = np.append(blue_vals, blue_win_other)
        red_vals = np.append(red_vals, red_win_other)

        blue_bans = Champion.get_champions(list(blue_win_top_10.keys()))
        red_bans = Champion.get_champions(list(red_win_top_10.keys()))

        fig.add_trace(go.Pie(
            name=ban,
            labels=blue_bans + ['Other'],
            values=blue_vals),
            row=1,
            col=1
        )

        fig.add_trace(go.Pie(
            name=ban,
            labels=red_bans + ['Other'],
            values=red_vals),
            row=1,
            col=2
        )

        fig.update_layout(
            height=600,
            width=900
        )

        #fig.show()

    '''
    
    Champs
    
    '''

    champs = ['blue_champ_1', 'blue_champ_2', 'blue_champ_3', 'blue_champ_4', 'blue_champ_5',
              'red_champ_1', 'red_champ_2', 'red_champ_3', 'red_champ_4', 'red_champ_5']

    champs_formatted = Champion.format_champs(df, champs, 35)

    fig = go.Figure(data=[
        go.Pie(
            labels=list(champs_formatted.keys()),
            values=list(champs_formatted.values())
        )
    ])

    fig.update_layout(
        height=900,
        width=900,
        title='Most Frequently Selected Champions'
    )

    fig.show()
