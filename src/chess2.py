import re
import pandas as pd
import time


def clean_pgns(pgn_games, path_out, evaluation=False):
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
            individual_moves_and_eval = re.findall(r'\d{1,2}\. ([\w-]+).+?{ \[%eval (-?\d{1,2}\.\d{1,2}).+?} \d{1,2}\.\.\. ([\w\-]+).+?{ \[%eval (-?\d{1,2}\.\d{1,2})', game_moves)
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

    df.to_csv(path_out, index=False, header=False, mode='a')
    print(len(pgn_games))


def load_split_data(regex_string, path_in, path_out_eval_games, path_out_non_eval_games, chunksize=10**9, eval_field=9):
    with open(path_in, 'r') as f:
        while True:
            read_data = f.read(chunksize)
            games = re.findall(r'{}'.format(regex_string), read_data)
            non_eval_games = []
            eval_games = []
            for game in games:
                if 'eval' in game[eval_field]:
                    eval_games.append(game)
                else:
                    non_eval_games.append(game)
            clean_pgns(eval_games, path_out_eval_games, evaluation=True)
            clean_pgns(non_eval_games, path_out_non_eval_games)
            if not read_data:
                break


regex_string_1000_1500_games_fixed = '(\[Site.+?\n)(?:.+?\n){0,4}(\[Result.+?\n)(?:.+?\n){0,2}(\[WhiteElo "1[0-4]\d\d"]\n)(\[BlackElo "1[0-4]\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+? 11\. .+?\d-\d\n)'

path_in_june_2018 = '/home/zackstrater/Downloads/lichess_data_june_2018'
path_out_june_2018_eval = '/media/zackstrater/New Volume/test_chess_data/eval_games'
path_out_june_2018_non_eval = '/media/zackstrater/New Volume/test_chess_data/non_eval_games'
load_split_data(regex_string_1000_1500_games_fixed, path_in_june_2018, path_out_june_2018_eval, path_out_june_2018_non_eval)









# all games (for finding out percentage of players in each elo and diff time controls)
# games = re.findall(
#             r'''(\[Result.+?\n)(?:.+?\n){2}(\[WhiteElo.+?\n)(\[BlackElo.+?\n)(\[WhiteRatingDiff.+?\n)(\[BlackRatingDiff.+?\n)(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl.+?\n)(\[Termination.+?\n)(\n1\..+?\d-\d\n)''', read_data)
#         print(len(games))

