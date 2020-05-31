# League of Legends Match Outcome Classifier
Using a data set of 10k Diamond and Master games with data from the first 10 min, along with the Riot Games API to get even more data about each game in the data set to predict the outcome of games.

The Jupyter Notebook equivalent of this README with interactive plots can be found here:  
https://www.kaggle.com/jbofill/league-of-legends-match-outcome-classifier

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

It is clear that the distribution of wards placed are left skewed, which may require a transformation.

![image](Charts/WardsPlacedZoom.png)

Here we can see that there is a slight trend with the amount of wards placed and a team winning. Usually the winning team has a larger amount of wards placed that game.

Both blue and red have a higher mean of wards placed when winning, but it is not that clear for blue side as it is with red.

### Wards Destroyed

Similar to wards being so important due to the information they can provide to the team, denying that information is also key to winning. Due to this idea, I would suspect that the team with more destroyed wards has a better chance of winning the game.

![image](Charts/WardsDestroyed.png)

In the range of 0-2 wards destroyed, there isn't a trend at all regarding the outcome of the game. Once the wards destroyed count exceeds 3, there is a clear trend that destroyed ward count correlates with winning. This is most likely due to the fact that if so many wards are destroyed that quickly, the team is dominating / being very aggressive and putting a lot of pressure on the other time.

### First Kills

First bloods are important because it provides gold for the team, which allows wards to be set up early. This will prevent the jungler from ganking as well.

![image](Charts/FirstBloods.png)

This bar graph takes the sum of games where a certain team got first blood. It is clear that teams that got a first kill are more likely to win, since it does provide advantages as stated earlier.
  
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
These are the 20 most frequent bans when a team wins. Unfortunately the API doesn't give information on who picked first, so when it says "Blue" or "Red" it just means the team that won
In th legend, the champions go in order of most frequent. For example, Other is the most banned, followed by Kassadin in Ban 1.
#### Ban 1
![image](Charts/bans/ban_1.png)
#### Ban 2 
![image](Charts/bans/ban_2.png)
#### Ban 3
![image](Charts/bans/ban_3.png)  
#### Ban 4 
![image](Charts/bans/ban_4.png)
#### Ban 5   
![image](Charts/bans/ban_5.png)
#### Ban 6 
![image](Charts/bans/ban_6.png)
#### Ban 7 
![image](Charts/bans/ban_7.png)
#### Ban 8  
![image](Charts/bans/ban_8.png)
#### Ban 9
![image](Charts/bans/ban_9.png)
#### Ban 10
![image](Charts/bans/ban_10.png)

It seems that people in diamond and master are not fond of Kassadin at all.
Generally, it seems that the ban selections are very strict at the top level of play.

### Champion Selections
#### Among Winning and Losing Teams
![image](Charts/MostSelectedChampions.png)
The idea presented by the pie chart makes sense, as usually team composition related games typically have metas between patches or seasons. So it makes sense to see champions that work best together to have pick rates close to one anothers.

#### Blue Winning
I suspect the choices to be relatively similar to the champion selection visualization embodying winning and losing teams
![image](Charts/ChampSelectionBlueWin_RedLose.png) 
It's interesting to see that Lee Sin is selected more on Red when they lose. I don't think this contributes to Red losing though.
#### Red Winning
![image](Charts/ChampSelectionRedWin_BlueLose.png)
Interesting that when blue loses, Lee Sin is very popular. At the same time, Lee Sin is the third most fequent pick when Red wins.

### First Inhibitor

Inhibitors are a very important structure in League of Legends because it prevents the opposition from training super minions in the lane with the inhibitor destroys. That having said, the team with a destroyed inhibitor would be put at a major disadvantage. I would suspect that teams win significantly more with a first inhibitor destroyed vs. not having destroyed an inhibitor first.

#### Blue Winning With and Without First Inhibitor
![image](Charts/BlueWin_FInhibitor_NoInhibitor.png)

Quite a difference. The data set is relatively small, but I am certain that if more data was added, the difference would still be large.

#### Red Winning With and Without First Inhibitor

![image](Charts/RedWin_FInhibitor_NoInhibitor.png)

Same result as Blue.

This means that destroying the inhibitor first is probably a good indicator of whether a team wins or not.

### First Baron

The Baron is the strongest monster in league due to providing the team that defeats it buffs including increased attack damage, increased ability power, and increases the power of minions.
Due to this, I suspect that this will also be a strong indicator of who wins the match.

![image](Charts/BlueWin_Baron_NoBaron.png)

It seems teams usually win more when getting the first baron, but the difference is not as severe as it is with inhibitors.

![image](Charts/RedWin_Baron_NoBaron.png)

The idea is the same as it is with Blue.

I would suspect that getting the first baron helps to lead to the first inhibitor if not destroyed already, which would help secure the game.

### Tower Kills

Since deaths in League can be detrimental to a team, I would assume that if one team dies a lot to towers that they would most likely lose the match.

![image](Charts/TowerKillsDist.png)

This was basically the distribution I had in mind. As a team suffers more deaths to towers, the less likely they win a game. I think this will also be a strong indicator of winning or losing if data values lie outside of 4-6 tower deaths

# Machine Learning

I will try using several different models in order to pick the most accurate result.

The process through which model selection will occur is by getting feature importance, hyperparameter tuning with 5 fold cv, then train test split to see which model performs the best.
 

## Feature Selection

![image](Charts/correlation_matrix.png)

Some features that will be removed regardless of correlation are: redFirstBlood, red_firstInhibitor, red_firstBaron, red_firstRiftHerald, and gameId just because we have the blue counter part to them and gameId is not necessary.

Other than those mentioned, I will keep everything else.

As for the features relating to champions, I will one hot encode all of them. This in return will give me a dataframe with really large dimensions, since there are 139 champions in league, and there are 15 champion related columns, the dimensions will grow very rapidly.

I plan to one hot encode the champion related columns, but this is problematic. There are currently 135 champions in League of Legends, this means that once I finish one hot encoding, I will have ~2025 extra columns added to my original data set. So I plan to try different methods of reducing the dimensionality and comparing their scores.

I would first like to try removing a certain amount of champions that are hardly used. I will set a threshold at 15 selections to be considered and see what happens.

##### After One Hot Encoding  
![image](Charts/beforeChampReduction.png)

##### After Removing champions selected < 15 times  
![image](Charts/AfterChampReduction.png)

So not bad, but the dimensionality is still really high. I may just try it anyways to see if PCA improves our results or worsens.

## Reducing Dimensionality  

After 3 days of training, I decided that the dimensions of the data were too high to continue and required research on how to handle this situation.

I began by looking into Logistic PCA, but unfortunately there are no Python packages for that. I would've made one myself had I known Linear Algebra (haven't taken that course yet, but soon I will)

I then looked into MCA, which deals with nominal values in data. I read some papers to grasp an understanding of Multiple Correspondence Analysis and decided this would be my approach to reducing the dimensionality of my data.

I plan to do a grid search on optimal components for MCA, but for now I am deciding to do 5 components for both champion selections (red and blue) and ban selections.

On top of this, I will experiment with applying log1p and PCA to my continuous data related columns to see how that effects the accuracy.

### After Applying MCA and PCA  
My dataframe now has the dimensions of 9879 x 26 This is a considerable improvement and the training process should be much quicker now.

### Normalizing Continuous Data
Since PCA assumes Gaussian, I am going to apply log1p transformations to the features with high skew values.

#### Skewness
![image](Charts/skewness.png)

The only features that will require transformations are blue/redWardsPlaced and blue/redTowersDestroyed.

#### Kurtosis
![image](Charts/Kurtosis.png)  
The same features that are very skewed also have high kurtosis.

#### After Log1p
![image](Charts/AfterLog1p.png)  
I would've liked blue/redTowers to be a little lower, but it should be OK.
The log transformation helped lower the Kurtosis score, but outliers are still very present in towers destroyed. 

This is fine though, as the reason for the outliers is that many times, no towers are destroyed within the first 10 min. That means that if one tower is destroyed, it is significant regarding whether a team wins or not.

## Model Selection
All models will have their hyperparameters tuned with a grid search and 5 fold cv.

So far, I have suspicion that Logistic Regression and XGBoost may be overfitting.
Since I have endless games to pull from, that would be the best way to test these models against data that has not been seen before.

### Logistic Regression

![image](Charts/logit_res.png)

Really high accuracy score. Potential overfitting

### XGBoost Classifier

Tuned hyperparameters with a grid search and 5 fold cv

![image](Charts/xgboost_res.png)  

The accuracy falls around 95% - 99%. I suspect overfitting as well, but I am going to mess with more models to see what happens.

## Model Selection Using Custom Test Data Set
Since I suspected my models might be overfitting, I grabbed 5k more games to add to my validation data set.
As of now, the models are being trained by 9879 games and are attempting to predict 5559 results.

I will discontinue the use of using the train test split, as I see no reason to use it since the validation set is twice as small as my custom test data set.

### Logistic Regression

![image](Charts/logit_custom.png)

The accuracy went down by 1% due to increasing the validation data set by more than double, which is pretty good.

### XGBoost Classifier

![image](Charts/xgboost_custom.png)

A huge performance drop with XGBoost, which is interesting. Originally, the model's accuracy was around 96% - 99%. It seems that XGBoost was overfitting to some degree.

### Random Forest Classifier

![image](Charts/RF_Results.png)

RF seems to be the model that performs the worst so far.

# Acknowledgements

[Multiple Corresdondence Analysis](https://www.researchgate.net/profile/Dominique_Valentin/publication/239542271_Multiple_Correspondence_Analysis/links/54a979900cf256bf8bb95c95.pdf) by Hervé Abdi & Dominique Valentin

[Variable Extractions using Principal Components
Analysis and Multiple Correspondence Analysis for
Large Number of Mixed Variables Classification
Problems](https://s3.amazonaws.com/academia.edu.documents/50782331/GJPAM_Published.pdf?response-content-disposition=inline%3B%20filename%3DVariable_Extractions_using_Principal_Com.pdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIATUSBJ6BAG7F36CVX%2F20200530%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200530T070022Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQD3gSoTHQ63nANvvqMflElvp2TbA9R7XSTkFbbPulMQ6QIgQgPJBUDeT5o%2BJsw5Pc7J7jWr4s38dLlCHw%2B1a8XY%2BAMqvQMI%2Fv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgwyNTAzMTg4MTEyMDAiDKwvShduLVGpTOEQUSqRA4XRIgf7eWeKKhYlHQzWolE5Vk1g9dfu73310GIKNjPIPqN5ocYMMnsJJkSPha4Cpbab41m6x3hIxjstzVkMBf8qa65WEE7vJA%2BWtPfntmgNieznvvb8fdEiEPjjwmHlFbbRDVw8WVboG5CvCBV2En1f3Audu1%2BVvOr3x6wfS1uJSQVPjYFP2cXkIr3wIJBDhqjWQZfl36pNHR%2BU2z5pTrn8jgQ0lgkiw%2Bnp01hJqnc3CsteBLcES5J1TgfPkBnBF2VfQECRuYejOkzyhq%2F8fsvP%2BIbEisjuzDiTgHqeWwIs%2BCXlZsiJLR1OK2iEd2hMl0gzUDXxl2yoqmkpv83AUchh%2BtORGjTJE7yA26MSX57aqeGZz%2Fqf1kj4Hj8pW4B7%2FUUcPXhpQ5ryDYKzyYtULzDCRQpif%2FjBUr1bZFj48jeIUY5bppEvyGsF8YJ5YiAS13jRysxz7FPG8XjoQm8%2BR84uYJqLsbNhBb0N3XMrisJ89er2DOg8iuoMH%2FWWBXIsdRjkFymb75xItgLipBEbFZqfMJLFx%2FYFOusBGpR9%2BtvXEK4vPfs95BDFzEu8kGK4pgB1M9PqxJPY9SzATCWo3%2FD3MDRC3OjWwbyZkhtYvehnipLldJwwjXNZAoQ%2BHJ2lwX8G8ZZMVvLkHb1Hp8WKhhOs4qEbaYrzbLgwi0UucN4yRw1Doi6BADo8k4fgZ1n5sVM0mH6mzPNpos%2BSuzm0lrVVd4SEQB1X7%2FEdiagrGzurSiVpMtCynpZzWnlKqWz10AcJS81KhZoLY%2FLbQiPWeutHOSZNvLVRzesqIx6wWoNliRH1yndEJhFC95IAuTT6fGphp6OFVACauf84tYzx5WMMYF0Csg%3D%3D&X-Amz-Signature=1365def7559093df3d23d4dae2e967cefb5f825fc808e02bc5095d18acc89b1d) by Hashibah Hamid, Nazrina Aziz, and Penny Ngu Ai Huong
