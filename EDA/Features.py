import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def feature_eda(df):

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

    #fig.show()

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

    #fig.show()

    '''
    
    First Bloods
    
    '''

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', x=blue_win['blueFirstBlood'], y=[np.sum(blue_win['blueFirstBlood'])]),
        go.Bar(name='Blue Loss', x=red_win['blueFirstBlood'], y=[np.sum(red_win['blueFirstBlood'])]),
        go.Bar(name='Red Win', x=red_win['redFirstBlood'], y=[np.sum(red_win['redFirstBlood'])]),
        go.Bar(name='Red Loss', x=blue_win['redFirstBlood'], y=[np.sum(blue_win['redFirstBlood'])])
    ])

    fig.update_layout(
        title='The Importance of First Kills',
        height=800,
        width=1200,
        xaxis=dict(
            showticklabels=False,
            title='Team'
        ),
    )

    #fig.show()

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

    #fig.show()

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

    #fig.show()


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
    #fig.show()

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

    #fig.show()

    fig = go.Figure(data=[
        go.Bar(name='Blue Win', y=[0], x=[np.sum(blue_win['blueEliteMonsters'])], width=0.5, orientation='h'),
        go.Bar(name='Blue Loss', y=[1], x=[np.sum(red_win['blueEliteMonsters'])], width=0.5, orientation='h'),
        go.Bar(name='Red Win', y=[2], x=[np.sum(red_win['redEliteMonsters'])], width=0.5, orientation='h'),
        go.Bar(name='Red Loss', y=[3], x=[np.sum(blue_win['redEliteMonsters'])], width=0.5, orientation='h')
    ])

    fig.update_layout(
        title='Epic Monsters Summoned when Winning and Losing',
        height=800,
        width=1200,
        yaxis=dict(
            tickvals=[i for i in range(4)],
            ticktext=[i for i in ['Blue Win', 'Blue Loss', 'Red Win', 'Red Loss']],
            showticklabels=True
        ),
    )

    #fig.show()

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

    #fig.show()


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

    #fig.show()

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

    #fig.show()

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

    #fig.show()

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

    #fig.show()








