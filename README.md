# LoL-MatchOutcome-Predictor
Using a data set of 10k Diamond and Master games along with the Riot Games API to get even more data about each game in the data set to predict the outcome of games.

# EDA

### Target

The target variable that I will attempt to determine is whether the team will win the game or not. In the data set, this is given as "blueWins", which really doesn't matter as we will be able to tell when red wins (if blue loses)

![image](Charts/Target.png)

It appears that wins and loses is distributed almost equally throughout the data set, which is good. This means I don't need to manually compensate for an uneven amount of wins/losses and essentially "guess" whether a team won or not just to make the distriubtion even.

Red has 4949 wins  
Blue has 4930 wins