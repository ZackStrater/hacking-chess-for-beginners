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
    first_five_moves = [[] for _ in range(10)]
    eval_first_five_moves = [[] for _ in range(10)]
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
            individual_move_pairs = re.findall(r'\d\d?\. (.+?) {.+?} \d{1,2}\.\.\. (.+?) {', game_moves)
            current_game_first_five_moves = []
            for i in range(5):
                current_game_first_five_moves.append(individual_move_pairs[i][0])
                current_game_first_five_moves.append(individual_move_pairs[i][1])
            for i in range(10):
                first_five_moves[i].append(current_game_first_five_moves[i])

        else:
            individual_moves_and_eval = re.findall(r'\d{1,2}\. ([\w\-+=#]+).+?{ \[%eval (-?\d{1,2}\.\d{1,2}|#\d{1,2}).+?} \d{1,2}\.\.\. ([\w\-+=#]+).+?{ \[%eval (-?\d{1,2}\.\d{1,2}|#\d{1,2})', game_moves)
            current_game_first_five_moves = []
            eval_current_game_first_five_moves = []
            for i in range(5):
                current_game_first_five_moves.append(individual_moves_and_eval[i][0])
                current_game_first_five_moves.append(individual_moves_and_eval[i][2])
                eval_current_game_first_five_moves.append(individual_moves_and_eval[i][1])
                eval_current_game_first_five_moves.append(individual_moves_and_eval[i][3])
            for i in range(10):
                first_five_moves[i].append(current_game_first_five_moves[i])
                eval_first_five_moves[i].append(eval_current_game_first_five_moves[i])

    if not evaluation:
        df = pd.DataFrame({'game_id': game_id, 'result': result, "white_elo": white_elo,
                           'black_elo': black_elo, 'white_rating_diff': white_rating_diff,
                           'black_rating_diff': black_rating_diff, 'eco': eco, 'opening': opening,
                           'time_control': time_control,
                           '1w': first_five_moves[0],
                           '1b': first_five_moves[1],
                           '2w': first_five_moves[2],
                           '2b': first_five_moves[3],
                           '3w': first_five_moves[4],
                           '3b': first_five_moves[5],
                           '4w': first_five_moves[6],
                           '4b': first_five_moves[7],
                           '5w': first_five_moves[8],
                           '5b': first_five_moves[9]
                           })
    else:
        df = pd.DataFrame({'game_id': game_id, 'result': result, "white_elo": white_elo,
                           'black_elo': black_elo, 'white_rating_diff': white_rating_diff,
                           'black_rating_diff': black_rating_diff, 'eco': eco, 'opening': opening,
                           'time_control': time_control,
                           '1w': first_five_moves[0],
                           '1b': first_five_moves[1],
                           '2w': first_five_moves[2],
                           '2b': first_five_moves[3],
                           '3w': first_five_moves[4],
                           '3b': first_five_moves[5],
                           '4w': first_five_moves[6],
                           '4b': first_five_moves[7],
                           '5w': first_five_moves[8],
                           '5b': first_five_moves[9],
                            'eval_1w': eval_first_five_moves[0],
                            'eval_1b': eval_first_five_moves[1],
                            'eval_2w': eval_first_five_moves[2],
                            'eval_2b': eval_first_five_moves[3],
                            'eval_3w': eval_first_five_moves[4],
                            'eval_3b': eval_first_five_moves[5],
                            'eval_4w': eval_first_five_moves[6],
                            'eval_4b': eval_first_five_moves[7],
                            'eval_5w': eval_first_five_moves[8],
                            'eval_5b': eval_first_five_moves[9]
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
            clean_pgns(eval_games, path_out_eval_games, evaluation=True)
            clean_pgns(non_eval_games, path_out_non_eval_games)
            if not read_data:
                break


regex_string_1000_1500_games = '(\[Site.+?\n)(?:.+?\n){0,4}(\[Result.+?\n)(?:.+?\n){0,2}(\[WhiteElo "1[0-4]\d\d"]\n)(\[BlackElo "1[0-4]\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+? 11\. .+?\d-\d\n)'


# path_in_june_2018 = '/home/zackstrater/Downloads/lichess_data_june_2018'
# path_out_june_2018_eval = '/media/zackstrater/New Volume/chess_data/lichess_data_june_2018_eval_games_cleaned'
# path_out_june_2018_non_eval = '/media/zackstrater/New Volume/chess_data/lichess_data_june_2018_cleaned'
# load_split_data(regex_string_1000_1500_games, path_in_june_2018, path_out_june_2018_eval, path_out_june_2018_non_eval)


# path_in_jan_2021 = '/media/zackstrater/New Volume/lichess_db_standard_rated_2021-01.pgn'
# path_out_jan_2021_eval = '/media/zackstrater/New Volume/chess_data/lichess_data_jan_2021_eval_games_cleaned'
# path_out_jan_2021_non_eval = '/media/zackstrater/New Volume/chess_data/lichess_data_jan_2021_cleaned'
# load_split_data(regex_string_1000_1500_games, path_in_jan_2021, path_out_jan_2021_eval, path_out_jan_2021_non_eval)


# regex_string_2000_plus_games = '(\[Site.+?\n)(?:.+?\n){0,4}(\[Result.+?\n)(?:.+?\n){0,2}(\[WhiteElo "2\d\d\d"]\n)(\[BlackElo "2\d\d\d"]\n)\[WhiteRatingDiff "([+-]\d\d?)"]\n\[BlackRatingDiff "([+-]\d\d?)"]\n(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl "300\+0"]\n)(?:\[Termination.+?\n)(\n1\..+? 11\. .+?\d-\d\n)'
# path_in_jan_2021 = '/media/zackstrater/New Volume/lichess_db_standard_rated_2021-01.pgn'
# path_out_jan_2021_eval = '/media/zackstrater/New Volume/chess_data/over_2000_lichess_data_jan_2021_eval_games_cleaned'
# path_out_jan_2021_non_eval = '/media/zackstrater/New Volume/chess_data/over_2000_lichess_data_jan_2021_cleaned'
# load_split_data(regex_string_2000_plus_games, path_in_jan_2021, path_out_jan_2021_eval, path_out_jan_2021_non_eval)

# all games (for finding out percentage of players in each elo and diff time controls)
# games = re.findall(
#             r'''(\[Result.+?\n)(?:.+?\n){2}(\[WhiteElo.+?\n)(\[BlackElo.+?\n)(\[WhiteRatingDiff.+?\n)(\[BlackRatingDiff.+?\n)(\[ECO.+?\n)(\[Opening.+?\n)(\[TimeControl.+?\n)(\[Termination.+?\n)(\n1\..+?\d-\d\n)''', read_data)
#         print(len(games))

