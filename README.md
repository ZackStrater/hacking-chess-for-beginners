# hacking-chess-for-beginners
Finding optimal chess openers for players rated 1000-1500


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
