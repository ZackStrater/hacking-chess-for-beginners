

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
    all_game_moves = []
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


        individual_move_pairs = re.findall(r'\d\d?\. (.+?) {.+?} \d{1,2}\.\.\. (.+?) {', game_moves)
        current_game_moves = ''
        for pair in individual_move_pairs:
            current_game_moves += pair[0] + ' '
            current_game_moves += pair[1] + ' '
        all_game_moves.append(current_game_moves)


    df = pd.DataFrame({'game_id': game_id, 'result': result, "white_elo": white_elo,
                       'black_elo': black_elo, 'white_rating_diff': white_rating_diff,
                       'black_rating_diff': black_rating_diff, 'eco': eco, 'opening': opening,
                       'time_control': time_control, 'all_game_moves': all_game_moves
                       })

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
            clean_pgns(non_eval_games, path_out_non_eval_games)
            if not read_data:
                break


# regex_string_1000_1500_games = '(\[Site.+?\n)(?:.+?\n){0,4}(\[Result "1-0"]\n)(?:.+?\n){0,2}(\[WhiteElo "1[0-4]\d\d"]\n)(\[BlackElo "1[0-4]\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+? 11\. .+?\d-\d\n)'
#
#
# path_in_jan_2021 = '/media/zackstrater/New Volume/lichess_db_standard_rated_2021-01.pgn'
# path_out_jan_2021_non_eval = '/media/zackstrater/New Volume/chess_data/white_wins_full_game_moves_lichess_data_jan_2021_cleaned'
# load_split_data(regex_string_1000_1500_games, path_in_jan_2021, None, path_out_jan_2021_non_eval)

regex_string_1000_1500_games = '(\[Site.+?\n)(?:.+?\n){0,4}(\[Result "\d-\d"]\n)(?:.+?\n){0,2}(\[WhiteElo "1[0-4]\d\d"]\n)(\[BlackElo "1[0-4]\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+? 11\. .+?\d-\d\n)'


path_in_jan_2021 = '/media/zackstrater/New Volume/lichess_db_standard_rated_2021-01.pgn'
path_out_jan_2021_non_eval = '/media/zackstrater/New Volume/chess_data/castled_lichess_data_jan_2021_cleaned'
load_split_data(regex_string_1000_1500_games, path_in_jan_2021, None, path_out_jan_2021_non_eval)

