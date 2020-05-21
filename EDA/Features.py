import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def feature_eda(df):

    blue_win = df[df['blueWins'] == 1]
    red_win = df[df['blueWins'] == 0]

    # Looking at wards placed

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

    # Wards destroyed

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

    fig.show()
