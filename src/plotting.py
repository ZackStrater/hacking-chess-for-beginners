


import pandas as pd


columns = ['game_id', 'result', "white_elo", 'black_elo', 'white_rating_diff',
           'black_rating_diff', 'eco', 'opening', 'time_control',
           '1w',
           '1b',
           '2w',
           '2b',
           '3w',
           '3b',
           '4w',
           '4b',
           '5w',
           '5b']
df = pd.read_csv('/media/zackstrater/New Volume/chess_data/lichess_data_jan_2021_cleaned',
                 names=columns)

pd.options.display.max_rows = 5000
import matplotlib.pyplot as plt




groups2 = df.groupby('opening').mean().reset_index()
groups3 = df.groupby('opening').count().reset_index()
gp2 = groups2.sort_values('opening')
gp3 = groups3.sort_values('opening')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2 = gp2[gp2['play_percent'] > 0.01]
gp2.head(10)


y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.3, s=20)
ax.set_ylim(-0.05, 4)
ax.set_xlabel("white win percent")
ax.set_ylabel("play percent")
plt.show()




df4 = df
df4['first_three_moves_white'] = df4['1w']+df4['1b']+df4['2w'] + df4['2b']+df4['3w']
df4['first_three_moves_black'] = df4['1w']+df4['1b']+df4['2w'] + df4['2b']+df4['3w'] + df['3b']
df4['first_two_moves_white'] = df4['1w']+df4['1b']+df4['2w']
df4['first_two_moves_black'] = df4['1w']+df4['1b']+df4['2w'] + df4['2b']




groups2 = df4.groupby('first_three_moves_white').mean().reset_index()
groups3 = df4.groupby('first_three_moves_white').count().reset_index()
gp2 = groups2.sort_values('first_three_moves_white')
gp3 = groups3.sort_values('first_three_moves_white')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2 = gp2[gp2['play_percent'] > 0.1]
gp2.head(10)

y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.3, s=20)
ax.set_ylim(-0.05, 4)
ax.set_xlabel("white win percent")
ax.set_ylabel("play percent")
plt.show()




groups2 = df4.groupby('first_three_moves_black').mean().reset_index()
groups3 = df4.groupby('first_three_moves_black').count().reset_index()
gp2 = groups2.sort_values('first_three_moves_black')
gp3 = groups3.sort_values('first_three_moves_black')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2 = gp2[gp2['play_percent'] > 0.1]
gp2.tail(10)


y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.3, s=20)
ax.set_ylim(-0.05, 4)
ax.set_xlabel("white win percent")
ax.set_ylabel("play percent")
plt.show()





groups2 = df4.groupby('first_two_moves_white').mean().reset_index()
groups3 = df4.groupby('first_two_moves_white').count().reset_index()
gp2 = groups2.sort_values('first_two_moves_white')
gp3 = groups3.sort_values('first_two_moves_white')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2 = gp2[gp2['play_percent'] > 0.5]
gp2.head(10)

y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.3, s=20)
ax.set_ylim(-0.05, 4)
ax.set_xlabel("white win percent")
ax.set_ylabel("play percent")
plt.show()





groups2 = df4.groupby('first_two_moves_black').mean().reset_index()
groups3 = df4.groupby('first_two_moves_black').count().reset_index()
gp2 = groups2.sort_values('first_two_moves_black')
gp3 = groups3.sort_values('first_two_moves_black')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2 = gp2[gp2['play_percent'] > 0.5]
gp2.tail(10)


y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.3, s=20)
ax.set_ylim(-0.05, 4)
ax.set_xlabel("white win percent")
ax.set_ylabel("play percent")
plt.show()