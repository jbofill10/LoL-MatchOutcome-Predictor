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

### Wards Destroyed

Similar to wards being so important due to the information they can provide to the team, denying that information is also key to winning. Due to this idea, I would suspect that the team with more destroyed wards has a better chance of winning the game.

![image](Charts/WardsDestroyed.png)

In the range of 0-2 wards destroyed, there isn't a trend at all regarding the outcome of the game. Once the wards destroyed count exceeds 3, there is a clear trend that destroyed ward count correlates with winning. This is most likely due to the fact that if so many wards are destroyed that quickly, the team is dominating / being very aggressive and putting a lot of pressure on the other time.

### First Kills

First bloods are important because it provides gold for the team, which allows wards to be set up early. This will prevent the jungler from ganking as well.

![image](Charts/FirstKills.png)

This bar graph takes the sum of games where a certain team got fiirst blood. It is clear that teams that got a first kill are more likely to win, since it does provide advantages as stated earlier.
  
But it is also possible that the team was just overall better and won regardless of the "first blood advantage".

### Team Kills
Kills in League are very important because it slows down the progression of your opponents build, along with giving you gold to upgrade your champion. For this reason, it is pretty clear that kills will be a very important indicator of whether a team wins or loses

![image](Charts/Kills.png)

The distribution of all the variations in this histogram are right skewed slightly.

![image](Charts/AvgKills.png)

As expected, teams that have more kills generally win more games.

### Team Deaths
If kills are vital to the success of a team, it must mean that survivability is also very important. This means that most likely the team that dies least has the higher chance of winning.

![image](Charts/TeamDeaths.png)

As suspected, Teams that win tend to die less on average.

### Assists

The team with more assists also means that team has more kills which should give them the advantage over their opponents. I expect the team with more assists to win more games
![image](Charts/Assists.png)

It is evident that teams with more assists end up winning more games.

### Towers Destroyed

Towers prevent the enemy team from attacking the Nexus. The more towers that are destroyed, the easier it becomes to attack the Nexus.  
Due to this idea, teams that win would have destoryed more towers than their opponents.

![image](Charts/TowersDestroyed.png)

In the first 10 min, usually no towers are destroyed. If one is destroyed, usually that team wins.

### Epic Monsters

Epic Monsters are important provide high gold/experience and buffs to the team that defeats them. This in turn provides an advantage for the team. I would expect to see that teams will win more on average if they kill more epic monsters.

![image](Charts/EpicMonsters.png)

Due to the rewards epic monsters provide, there is a definite advantage to the team with more monster kills.

### Total Experience

The more experience a champion has earned, the stronger the build the champion will have. Therefore teams that win will most likely have more experience.

![image](Charts/TotalExperience.png)

### Total Gold

Stronger items and upgrades to items can be obtained with gold. So most likely the teams that win will have more gold since they had stronger champions that contributed to winning the game.

![image](Charts/TotalGold.png)

### CS Per Min

Creep Score, or CS, is one of the most important aspects of League. Having a good creep score means a reliable and steady amount of income, which is pointed out earlier is very important for winning games. Due to this, I know for sure that the winning teams will have higher CS than the losing teams.

![image](Charts/CSPerMin.png)

### Champion Bans

#### When Blue Wins
![image](Charts/bans/blue/ban_1.png) ![image](Charts/bans/blue/ban_2.png)  
![image](Charts/bans/blue/ban_3.png) ![image](Charts/bans/blue/ban_4.png)  
![image](Charts/bans/blue/ban_5.png) ![image](Charts/bans/blue/ban_6.png)  
![image](Charts/bans/blue/ban_7.png) ![image](Charts/bans/blue/ban_8.png)  
![image](Charts/bans/blue/ban_9.png) ![image](Charts/bans/blue/ban_10.png)  
 
It seems that people in diamond and master are not fond of Kassadin at all. I would assume that bans when red team wins will consist of the same champions in these bans

#### When Red Wins
![image](Charts/bans/red/ban_1.png) ![image](Charts/bans/red/ban_2.png)  
![image](Charts/bans/red/ban_3.png) ![image](Charts/bans/red/ban_4.png)  
![image](Charts/bans/red/ban_5.png) ![image](Charts/bans/red/ban_6.png)  
![image](Charts/bans/red/ban_7.png) ![image](Charts/bans/red/ban_8.png)  
![image](Charts/bans/red/ban_9.png) ![image](Charts/bans/red/ban_10.png) 

As expected, the same 5 champions were shown again. 
