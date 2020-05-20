import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def feature_eda(df):
    blue_win = df[df['blueWins'] == 1]
    red_win = df[df['blueWins'] == 0]

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

    fig.show()


