# LoL-MatchOutcome-Predictor
Using a data set of 10k Diamond and Master games along with the Riot Games API to get even more data about each game in the data set to predict the outcome of games.

# EDA

### Target

The target variable that I will attempt to determine is whether the team will win the game or not. In the data set, this is given as "blueWins", which really doesn't matter as we will be able to tell when red wins (if blue loses)

![image](Charts/Target.png)

It appears that wins and loses is distributed almost equally throughout the data set, which is good. This means I don't need to manually compensate for an uneven amount of wins/losses and essentially "guess" whether a team won or not just to make the distriubtion even.

Red has 4949 wins  
Blue has 4930 wins

### Wards Placed

Having more information than your opponent in any game is one of the biggest advantages a team can have over another. Therefore, wards are extremely important for the success of a team as they grant extra vision of the enemy and map.

![image](Charts/WardsPlaced.png)

On average, about 20 wards a game are placed. It is interesting and mind boggling how some games have up to 276 wards placed.

It is clear that the distribution of wards placed is left skewed and will require a transformation before fitting the data to a model.

![image](Charts/WardsPlacedZoom.png)

Here we can see that there is a slight trend with the amount of wards placed and a team winning. Usually the winning team has a larger amount of wards placed that game.

Both blue and red have a higher mean of wards placed when winning, but it is not that clear for blue side as it is with red.
