


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
ax.set_xlabel("white win percent")
ax.set_ylabel("play percent")
plt.show()






groups2 = df4.groupby('1w').mean().reset_index()
groups3 = df4.groupby('1w').count().reset_index()
gp2 = groups2.sort_values('1w')
gp3 = groups3.sort_values('1w')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2.head(10)


y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.3, s=20)
ax.set_ylim(-0.05, 4)
ax.set_xlabel("white win %")
ax.set_ylabel("play %")
plt.show()


y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(x, y, alpha=1, s=20)
ax.set_ylim(-10, 70)
ax.set_xlim(0.42, 0.55)
ax.set_xlabel("white win %")
ax.set_ylabel("play %")
ax.annotate(gp2['1w'][0], (x[0], y[0]), textcoords="offset points", xytext=(-10, 10))
ax.annotate(gp2['1w'][1], (x[1], y[1]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1w'][2], (x[2], y[2]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1w'][3], (x[3], y[3]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1w'][4], (x[4], y[4]), textcoords="offset points", xytext=(-15, -15))
ax.annotate(gp2['1w'][5], (x[5], y[5]), textcoords="offset points", xytext=(-15, -15))
ax.annotate(gp2['1w'][6], (x[6], y[6]), textcoords="offset points", xytext=(10, 0))
ax.annotate(gp2['1w'][7], (x[7], y[7]), textcoords="offset points", xytext=(5, 5))
ax.annotate(gp2['1w'][8], (x[8], y[8]), textcoords="offset points", xytext=(10, 0))
ax.annotate(gp2['1w'][9], (x[9], y[9]), textcoords="offset points", xytext=(10, 10))
ax.annotate(gp2['1w'][10], (x[10], y[10]), textcoords="offset points", xytext=(-10, 10))
ax.annotate(gp2['1w'][11], (x[11], y[11]), textcoords="offset points", xytext=(10, 0))
ax.annotate(gp2['1w'][12], (x[12], y[12]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1w'][13], (x[13], y[13]), textcoords="offset points", xytext=(10, 0))
ax.annotate(gp2['1w'][14], (x[14], y[14]), textcoords="offset points", xytext=(10, 0))
ax.annotate(gp2['1w'][15], (x[15], y[15]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1w'][16], (x[16], y[16]), textcoords="offset points", xytext=(-15, -15))
ax.annotate(gp2['1w'][17], (x[17], y[17]), textcoords="offset points", xytext=(-15, -15))
ax.annotate(gp2['1w'][18], (x[18], y[18]), textcoords="offset points", xytext=(10, 0))
ax.annotate(gp2['1w'][19], (x[19], y[19]), textcoords="offset points", xytext=(0, 10))
plt.show()




y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(x, y, alpha=1, s=20)
ax.set_ylim(-9, 55)
ax.set_xlim(0.49, 0.55)
ax.set_xlabel("white win %")
ax.set_ylabel("play %")
for i, txt in enumerate(gp2['1b']):
    if i not in [2, 11, 19]:
        ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1b'][2], (x[2], y[2]), textcoords="offset points", xytext=(0, 10))
ax.annotate(gp2['1b'][11], (x[11], y[11]), textcoords="offset points", xytext=(5, -10))
ax.annotate(gp2['1b'][19], (x[19], y[19]), textcoords="offset points", xytext=(-20, 0))
plt.show()