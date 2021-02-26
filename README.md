# hacking-chess-for-beginners
The player base for online chess has exploded over the last 10 years, due to the rise of free to play chess websites that allow you to play with players from around the world ----

Chess is well known for being one of the most strategically difficult and complex games.  Even the opening few moves of a chess game, which might seem relatively limited at first glance, demonstrates how astronomically diverse the game is.  By the time both players have taken 3 turns each (each pair of turns is referred to as one move), the number of possible board states is around 120 million.  This dense thicket of possibilties can be an incredibly daunting for new players and as such beginners (like myself!) tend to stick to just one or two openings.  Yet, learning specific chess openings can be incredibly important to improving and is one of the first things that beginners are instructed to learn after learning the basics.  However, advice on what openings to learn is often coming from the perspective of teachers and more experienced players.  I wanted to know what are the openings for beginner level players that statistically lead to the highest win percentage both from black and white side.  Are there openings that would lead to significantly higher winrates for these players?

## Data
The data for this project came from the public database from lichess.org, a popular free online chess site.  I collected all of the game data January 2021, which consisted of almost 100 million games.  For the majority of my analysis I filtered this data by elo rating (a score that approximates a players skill relative to the rest of the playerbase), looking specifically at the 1000-1500 elo range, which is generally considered the range between beginner and intermediate, where learning openings starts to become important.  For comparison, the 0-1000 elo range typically encompasses players that are learning the fundementals of chess while the highest rated chess grandmasters can be rated well above 3000 elo.  The 1000-1500 elo range encompasses nearly half of the playerbase and is a where a lot of chess learners get "stuck" (like me!)

Additionally, selected only games played in the 5 minute time format as it is one of the most popular and is long enough for opening selection to have a large effect on the game.

Analysis


## proposal
# dataset: Lichess.org monthly games database
	https://database.lichess.org/
# This project aims to elucidate which chess openings are best for boosting the winning odds for chess beginners.
The player base for online chess has exploded over the last 10 years, due to the rise of free to play chess websites that allow you to play with players from around the world.  One of the most important features that online chess brings to casual players is the implementation of the elo rating system, which gives players a constantly updating numerical value that represents their approximate skill level.  Because ratings are a source of great pride (or shame) for chess players, finding simple ways to increase peoples’ ratings would be a valuable export.  
My plan is to analyze the chess games of players rated 1000-1500 and see if certain chess openings lead to a higher win percent (null hypothesis: win chances are independent of the opening moves).   The data will be pulled from the lichess database, which records tens of millions of games each month.  The includes all the moves in the games, which side won, the elo rating of each player, as well ass the name of the opening.
# MVP: 
determine if there are chess openings that lead to statistically significant increase in winning odds.  Find the top openers for both black and white that lead to the highest differential in overall win rate.  Do these openers have anything in common (are they safe openers, or more aggressive? Are they more positional or tactical in nature?)
# MVP++: 
Find openers that both have a high win rate and that are likely to occur (openers are determined by both players after all!).   Additionally, break down more the openings further by rating (1000, 1100, 1200, etc..).  Are there better openings for players above vs below your current rating?  As the dataset includes computer evaluation, also look for openers that consistently lead to highly advantageous positions and find common lines for each opening that lead to those advantages.
# MVP++: 
Run a simulation in which multiple players compete to raise their elo rating.   Match outcomes are solely determined by the probabilities found in the match data.  A control group selects openers at the same rate as the overall population, while a test group tries to force advantageous openers.  The experiment will test whether trying to force certain openers will lead to an increase in elo rating compared to the control group.    
