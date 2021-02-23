import re
import pandas as pd
import time


def clean_pgns(pgn_games, path, evaluation=False):
    # bins for each capture group
    game_id = []
    result = []
    white_elo = []
    black_elo = []
    white_rating_diff = []
    black_rating_diff = []
    eco = []
    opening = []
    time_control = []
    first_ten_moves = []
    eval_first_ten_moves = []
    for game in pgn_games:
        game_id.append(game[0][7:-3])
        result.append(game[1][9])  # 1 = White win, 0 = Black win
        white_elo.append(game[2][11:15])
        black_elo.append(game[3][11:15])
        white_rating_diff.append(game[4])
        black_rating_diff.append(game[5])
        eco.append(game[6][6:9])
        opening.append(game[7][10:-3])
        time_control.append(game[8][14:19])
        game_moves = game[9][1:-5]

        if not evaluation:
            individual_move_pairs = re.findall(r'\d\d?\. (.+?) {.+?} (.+?) {', game_moves)
            current_game_first_ten_moves = []
            for i in range(5):
                current_game_first_ten_moves.append(individual_move_pairs[i][0])
                current_game_first_ten_moves.append(individual_move_pairs[i][1])
            first_ten_moves.append(current_game_first_ten_moves)
        else:
            individual_moves_and_eval = re.findall(r'\d{1,2}\. ([\w-]+).+?{ \[%eval (-?\d\.\d{1,2}).+?} \d{1,2}\.\.\. ([\w\-]+).+?{ \[%eval (-?\d\.\d{1,2})', game_moves)
            current_game_first_ten_moves = []
            eval_current_game_first_ten_moves = []
            for i in range(5):
                current_game_first_ten_moves.append(individual_moves_and_eval[i][0])
                current_game_first_ten_moves.append(individual_moves_and_eval[i][1])
                eval_current_game_first_ten_moves.append(individual_moves_and_eval[i][1])
                eval_current_game_first_ten_moves.append(individual_moves_and_eval[i][3])
            first_ten_moves.append(current_game_first_ten_moves)
            eval_first_ten_moves.append(eval_current_game_first_ten_moves)


    df = pd.DataFrame({'game_id': game_id, 'result': result, "white_elo": white_elo,
                       'black_elo': black_elo, 'white_rating_diff': white_rating_diff,
                       'black_rating_diff': black_rating_diff, 'eco': eco, 'opening': opening,
                       'time_control': time_control, 'first_ten_moves': first_ten_moves,
                       })

    if evaluation:
        df['eval_first_ten_moves'] = eval_first_ten_moves
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)  # or 199
    print(df)

    df.to_csv(path, index=False, header=False, mode='a')
    print(len(pgn_games))


chunksize = 10**8
with open('/home/zackstrater/Downloads/lichess_data_june_2018', 'r') as f:
    while True:
        read_data = f.read(chunksize)
        games = re.findall(
            #               noncaptured lines             noncaptured lines   Only games where Elo between 1000-15000                                                                                                            only 5 minute games                              only games past 10 moves
            r'''(\[Site.+?\n)(?:.+?\n){0,4}(\[Result.+?\n)(?:.+?\n){0,2}(\[WhiteElo "1[0-4]\d\d"]\n)(\[BlackElo "1[0-4]\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+? 11\. .+?\d-\d\n)''', read_data)
        non_eval_games = []
        eval_games =[]
        for game in games:
            if 'eval' in game[9]:
                eval_games.append(game)
            else:
                non_eval_games.append(game)
        #clean_pgns(eval_games, '/media/zackstrater/New Volume/chess_data/lichess_data_june_2018_cleaned', evaluation=True)
        clean_pgns(non_eval_games, '/media/zackstrater/New Volume/chess_data/lichess_data_june_2018_cleaned')
        if not read_data:
            break





# seeing the most popular time formats (kinda)
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

