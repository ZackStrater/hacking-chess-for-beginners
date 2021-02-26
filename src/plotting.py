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
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt

# adding first_three moves column
df4 = df
df4['first_three_moves_white'] = df4['1w']+df4['1b']+df4['2w'] + df4['2b']+df4['3w']
df4['first_three_moves_black'] = df4['1w']+df4['1b']+df4['2w'] + df4['2b']+df4['3w'] + df['3b']
df4['first_two_moves_white'] = df4['1w']+df4['1b']+df4['2w']
df4['first_two_moves_black'] = df4['1w']+df4['1b']+df4['2w'] + df4['2b']


# group by and plot first white move
groups2 = df4.groupby('1w').mean().reset_index()
groups3 = df4.groupby('1w').count().reset_index()
gp2 = groups2.sort_values('1w')
gp3 = groups3.sort_values('1w')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2.sort_values('result', ascending = False, inplace=True)
gp2.head(20)
y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(x, y, alpha=0.5, s=25)
ax.set_ylim(-9, 70)
ax.set_xlabel("white win %")
ax.set_ylabel("play %")
ax.annotate(gp2['1w'][0], (x[0], y[0]), textcoords="offset points", xytext=(-10, 10), size= 12)
ax.annotate(gp2['1w'][1], (x[1], y[1]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.annotate(gp2['1w'][2], (x[2], y[2]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.annotate(gp2['1w'][3], (x[3], y[3]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.annotate(gp2['1w'][4], (x[4], y[4]), textcoords="offset points", xytext=(-15, -15), size= 12)
ax.annotate(gp2['1w'][5], (x[5], y[5]), textcoords="offset points", xytext=(-15, -15), size= 12)
ax.annotate(gp2['1w'][6], (x[6], y[6]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1w'][7], (x[7], y[7]), textcoords="offset points", xytext=(5, 5), size= 12)
ax.annotate(gp2['1w'][8], (x[8], y[8]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1w'][9], (x[9], y[9]), textcoords="offset points", xytext=(5, 10), size= 12)
ax.annotate(gp2['1w'][10], (x[10], y[10]), textcoords="offset points", xytext=(-10, 10), size= 12)
ax.annotate(gp2['1w'][11], (x[11], y[11]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1w'][12], (x[12], y[12]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.annotate(gp2['1w'][13], (x[13], y[13]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1w'][14], (x[14], y[14]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1w'][15], (x[15], y[15]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.annotate(gp2['1w'][16], (x[16], y[16]), textcoords="offset points", xytext=(-15, -15), size= 12)
ax.annotate(gp2['1w'][17], (x[17], y[17]), textcoords="offset points", xytext=(-15, -15), size= 12)
ax.annotate(gp2['1w'][18], (x[18], y[18]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1w'][19], (x[19], y[19]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.set_title('White First Moves')
fig.savefig('/home/zackstrater/DSIclass/hacking-chess-for-beginners/images/white_first_moves_plot.png', bbox_inches = 'tight')
plt.show()






# group and plot by first black move
groups2 = df4.groupby('1b').mean().reset_index()
groups3 = df4.groupby('1b').count().reset_index()
gp2 = groups2.sort_values('1b')
gp3 = groups3.sort_values('1b')

gp2['play_percent'] = gp3['game_id']/3929420*100
gp2['result'] = 1-gp2['result']
gp2.sort_values('result', ascending = False, inplace=True)
gp2.reset_index(drop=True, inplace=True)
gp2.head(20)


y = gp2['play_percent']
x = gp2['result']
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(x, y, alpha=0.5, s=25)
ax.set_ylim(-9, 55)

ax.set_xlabel("black win %")
ax.set_ylabel("play %")
for i, txt in enumerate(gp2['1b']):
    if i not in [2, 3, 6, 7, 10, 19]:
        ax.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), size= 12)
ax.annotate(gp2['1b'][2], (x[2], y[2]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1b'][3], (x[3], y[3]), textcoords="offset points", xytext=(-15, -15), size= 12)
ax.annotate(gp2['1b'][6], (x[6], y[6]), textcoords="offset points", xytext=(10, 0), size= 12)
ax.annotate(gp2['1b'][7], (x[7], y[7]), textcoords="offset points", xytext=(-15, -15), size= 12)
ax.annotate(gp2['1b'][19], (x[19], y[19]), textcoords="offset points", xytext=(5, 0), size= 12)
ax.annotate(gp2['1b'][10], (x[10], y[10]), textcoords="offset points", xytext=(10, -10), size= 12)
ax.set_title('Black First Moves')
fig.savefig('/home/zackstrater/DSIclass/hacking-chess-for-beginners/images/black_first_moves_plot.png', bbox_inches = 'tight')
plt.show()