import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt


def target_eda(df):
    fig = go.Figure()
    blueWins = df[df['blueWins'] == 1]
    blueLoss = df[df['blueWins'] == 0]

    fig.add_trace(go.Bar(x=blueWins['blueWins'], y=list(blueWins['blueWins'].value_counts()), name='Blue', marker_color='#0045D7'))
    fig.add_trace(go.Bar(x=blueLoss['blueWins'], y=list(blueLoss['blueWins'].value_counts()), name='Red',
                         marker_color=['#FD000D']))

    fig.update_layout(
        xaxis=dict(
            showticklabels=False,
            title='Team'
        ),
        yaxis_title='Wins',
        title='Wins From Each Team',
        height=800,
        width=1200
    )

    fig.show()
