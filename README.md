# Punt Kings

Generate a competitive edge in your 9-Cat Fantasy Basketball league.

![NBA Allstars](img/nba_allstars.jpeg)


### What is Punt Kings?

The goal of Punt Kings is to provide fantasy basketball managers a platform to optimize their roster with a competitive 
edge in 9 category (9-Cat) formats.

##### The Process:

1) Project individual player performances for the upcoming NBA season.
2) Construct a statistical strengths/weaknesses profile for each player.
3) Provide an interactive draft tool that presents the best available player information, overall team 
strengths  and weaknesses relative to the rest of the league, and the type of statistics to target in any given
round all simultaneously during a fantasy draft. 


### What is a 9-Cat format in fantasy basketball?

Unlike fantasy football or points format fantasy basketball that uses a standardized point system for all statistics,
**9-Cat format compartmentalizes a head to head match-up into 9 different categories based on 9 basketball 
statistics in an NBA game**. Every fantasy team in a weekly match-up battles to win out the majority of the 9 categories.

The 9 categories aggregated from weekly match-ups are:

1) Field Goal Percentage (FG%)
2) Free Throw Percentage (FT%)
3) Three Points Made (3PM)
4) Points (PTS)
5) Rebounds (REB)
6) Assists (AST)
7) Steals (STL)
8) Blocks (BLK)
9) Turnovers (TO)

For every category a team edges the other team in, the team is awarded 1 point. 

Example: Team A vs. Team B

Team A wins the categories:
1) FT% (higher percentage than Team B)
2) 3PM (more 3 pointers made than Team B)
3) PTS (scored more points than Team B)
4) AST (tallied more assists than Team B)
5) STL (more steals than Team B)

Team B wins the categories:
1) FG% (higher percentage than Team A)
2) REB (collected more rebounds than Team A)
3) BLK (blocked more shots than Team A)
4) TO (generated less turnovers than Team A)

***Team A wins 5-4.***

*Depending on your league settings, your overall season record is either 1) aggregated by your weekly score (Team A would 
have an overall record of 5-4 and Team B, 4-5) or 2) a win is 1-0, a loss is 0-1, and a tie is 0-0-1.*


To win in 9-Cat fantasy basketball you must have the best overall record, beating out opponents in head to head 
match-ups by winning majority of the 9 categories, and more importantly making the playoffs and winning every match-up
to secure a championship victory!


### What is "punting" and why use a "punting" strategy?

##### The What
- Implementing a "punting" strategy is where the competitive edge comes into play for your fantasy team. 
- Instead of spreading out your team thin by ambitiously attempting to be good in all 9 categories, 
the idea of punting is to focus your team build on certain categories, and in effect "punting" or better word "avoiding"
other categories of the 9 total categories.
##### The Why
- When building a team and focusing on 8, 7, or 6 specific categories (depending on personal preference/strategy),
you are effectively GREAT at those focused categories, making your team dangerous in a head to head match-up 
to win majority of the categories on a weekly basis.
- When focusing on specific categories, you will in effect "punt" or "defer" other categories.

##### Important Notes for Punting
- "Punting" is a strategy that has been used by many experienced managers in previous years, but Punt Kings is here
to make this process user-friendly for anyone no matter the experience/knowledge.
- Punt Kings is created to help identify optimal value in team builds and to correctly focus the user's 
attention in categories of the user's choice.
- "Punting" is also commonly mistaken as "wanting to be BAD in a category". That is far from what punting accomplishes.
When managers focus on the category they want to avoid, they effectively miss out on a player that provides good value
in other categories you may need in your team build. 
- There is a fine line to punting and if not careful you could end up being unstoppable in 4 categories, but struggle
to be competitive in 5 other categories. 
- This is way optimization and tracking of team stats is crucial, and why Punt Kings will provide value to fantasy 
managers that want a competitive edge in their respective leagues. 

---


## The Data Science Process
### The Data

[screencap on basketball reference page 2019 season stats]

scraping data from basketball reference

nba season 1990 to present.


#### Data Preparation (Modeling Logic / Plan)


Create a model for each predictive stat
Fit different models and extract the best performing model for each category.




#### Results

Predicting: PTS

Lasso model RMSE: 298.381
Baseline model RMSE: 337.60976640039905


Predicting: FG

Lasso model RMSE: 111.4656
Baseline model RMSE: 125.46233914481796


Predicting: FGA

Lasso model RMSE: 235.582
Baseline model RMSE: 260.4556686651412


Predicting: 3P

LR model RMSE: 29.4272
Baseline model RMSE: 42.84477514565286


Predicting: 3PA

LR model RMSE: 74.2045
Baseline model RMSE: 109.16275592688835


Predicting: FT

LR model RMSE: 66.251
Baseline model RMSE: 62.51260067153219


Predicting: FTA

LR model RMSE: 84.0169
Baseline model RMSE: 79.28739049345826


Predicting: ORB

LR model RMSE: 41.5894
Baseline model RMSE: 37.56127679623134


Predicting: DRB

LR model RMSE: 94.0248
Baseline model RMSE: 111.62634880516703


Predicting: AST

LR model RMSE: 74.7995
Baseline model RMSE: 81.07959352042222


Predicting: STL

LR model RMSE: 23.8926
Baseline model RMSE: 25.377872404261755


Predicting: BLK

LR model RMSE: 22.466
Baseline model RMSE: 21.12675568622032


Predicting: TOV

LR model RMSE: 40.7704
Baseline model RMSE: 42.269046950423274


Predicting: G

LR model RMSE: 20.2908
Baseline model RMSE: 24.67246608112517


Predicting: GS

Lasso model RMSE: 21.7821
Baseline model RMSE: 25.2627455095366


Predicting: MP

Lasso model RMSE: 636.6764
Baseline model RMSE: 695.98160755745





---

### Punt Kings Draft Tool

[scraping yahoo data draft results real time]

[compare an optimized (w/ adp) lineup using some punt strategy vs a "stacked" 
team that do not work together (show their adp)]


Draft strategy (concept of extracting optimal value on a per round basis)

Catergorical awareness (use this tool to understand a player's strength and weakness)




---

###Future Work

1) Add more features to data for modeling (draft class? age? ligament-type injury history?)
2) Need a way to understand a player coming off an injury
3) Predictions for rookies
4) Add a human element to projections (understanding/projecting impact of player team and if usage is trending up
add a sentiment factor for each player.)