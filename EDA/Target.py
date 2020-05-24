import plotly.graph_objs as go
import seaborn as sns
import matplotlib.pyplot as plt


def target_eda(df):
    fig = go.Figure()
    blue_wins = df[df['blueWins'] == 1]
    blue_loss = df[df['blueWins'] == 0]

    fig.add_trace(go.Bar(x=[0], y=list(blue_wins['blueWins'].value_counts()), name='Blue', marker_color='#084177', width=0.5))
    fig.add_trace(go.Bar(x=[1], y=list(blue_loss['blueWins'].value_counts()), name='Red',
                         marker_color=['#d63447'], width=0.5))

    fig.update_layout(
        xaxis=dict(
            showticklabels=True,
            tickvals=[0, 1],
            ticktext=[i for i in ['Blue', 'Red']],
        ),
        yaxis_title='Wins',
        title='Wins From Each Team',
        height=800,
        width=1200
    )

    #fig.show()
