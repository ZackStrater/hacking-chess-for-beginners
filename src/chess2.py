import re
import pandas as pd


total = 0
chunksize = 10**9
with open('/home/zackstrater/Downloads/lichess_data_june_2018', 'r') as f:
    while True:
        read_data = f.read(chunksize)
        games = re.findall(   # make capturing groups better so you don't have to edit later
            r'''(\[Site.+?\n)(?:.+?\n){0,4}(\[Result.+?\n)(?:.+?\n){0,22}(\[WhiteElo "1[0-4]\d\d"]\n)(\[BlackElo "1[0-4]\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+?\d-\d\n)''', read_data)
        game_id = []
        result = []
        white_elo = []
        black_elo = []
        white_rating_diff = []
        black_rating_diff = []
        eco = []
        opening = []
        time_control = []
        moves = []
        for game in games:
            game_id.append(game[0][7:-3])
            result.append(game[1][9]) # 1 = White win, 0 = Black win
            white_elo.append(game[2][11:15])
            black_elo.append(game[3][11:15])
            white_rating_diff.append(game[4])
            black_rating_diff.append(game[5])
            eco.append(game[6][6:9])
            opening.append(game[7][10:-3])
            time_control.append(game[8][14:19])
            moves.append(game[9][1:-5])

        df = pd.DataFrame({'game_id': game_id, 'result': result, "white_elo": white_elo,
                           'black_elo': black_elo, 'white_rating_diff': white_rating_diff,
                           'black_rating_diff': black_rating_diff, 'eco': eco, 'opening': opening,
                           'time_control': time_control, 'moves': moves
                           })
        # pd.set_option('display.max_columns', None)  # or 1000
        # pd.set_option('display.max_rows', None)  # or 1000
        # pd.set_option('display.width', None)
        # pd.set_option('display.max_colwidth', None)  # or 199
        # print(df)

        df.to_csv('/media/zackstrater/New Volume/chess_data/lichess_data_june_2018_cleaned', index=False, header=False, mode='a')
        print(len(games))
        total += len(games)
        if not read_data:
            break

print(total)


# from collections import Counter
# time_dict ={}
# for k, v in Counter(time_control).items():
#     if v / 140000 * 100 > 9:
#         if k not in time_dict:
#             time_dict[k] = v / 140000 * 100
#         else:
#             time_dict[k] = (time_dict[k] + v / 140000 * 100) / 2
# print(time_dict)


# all games (for finding out percentage of players in each elo and diff time controls)
# games = re.findall(
#             r'''(\[Result.+?\n)(?:.+?\n){2}(\[WhiteElo.+?\n)(\[BlackElo.+?\n)(\[WhiteRatingDiff.+?\n)(\[BlackRatingDiff.+?\n)(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl.+?\n)(\[Termination.+?\n)(\n1\..+?\d-\d\n)''', read_data)
#         print(len(games))

