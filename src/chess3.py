import chess
import chess.engine
import numpy as np
print(np.version.version)

chess_dict = {
    'R': 1,
    'N': 2,
    'B': 3,
    'K': 4,
    'Q': 5,
    'P': 6,
    'r': -1,
    'n': -2,
    'b': -3,
    'k': -4,
    'q': -5,
    'p': -6,
    0: 0
    }




def convert_board_to_array(board_state):
    piece_positions = {k:str(v) for k,v in board_state.piece_map().items()}

    for i in range(64):
        if i not in piece_positions:
            piece_positions[i] = 0

    board_pieces_list = [chess_dict[piece_positions[i]] for i in (range(64))]
    board_array =  np.array(board_pieces_list).reshape(8,8)
    return np.flip(board_array, axis=0)

def isolate_move(current_board_state_array, previous_board_state_array, move_color):
    if move_color == 'w':
        # parts of board that did not change are now 0
        difference_array = current_board_state_array - previous_board_state_array
        # we only care about where pieces moved to.  White moves leave a negative num in the square the moved from
        # this returns those squares back to 0:
        difference_array[difference_array < 0] = 0
        # when pieces are captured the destination square will be sum of value of white and black pieces
        # to correct, we find the index of the square that changed (just the destination square of white piece)
        move_index = np.nonzero(difference_array)
        # return this square to the original value of the piece that moved
        # this fixes en passant, castling shows both rook and king moving
        difference_array[move_index] = current_board_state_array[move_index]
        return difference_array
    elif move_color == 'b':
        difference_array = current_board_state_array - previous_board_state_array
        difference_array[difference_array > 0] = 0
        move_index = np.nonzero(difference_array)
        difference_array[move_index] = current_board_state_array[move_index]
        return difference_array

    else:
        return None


def compile_moves(moves, move_cutoff=0):
    board = chess.Board()
    raw_move_array_bin = [convert_board_to_array(board)] # initialized with starting board position
    for i in range(len(moves)):
        board.push_san(moves[i])
        board_state_array = convert_board_to_array(board)
        raw_move_array_bin.append(board_state_array)

    isolated_move_array_bin = []
    for i in range(1, len(raw_move_array_bin)):
        if i % 2 != 0:
            isolated_move_array_bin.append(isolate_move(raw_move_array_bin[i], raw_move_array_bin[i-1], 'w'))
        else:
            isolated_move_array_bin.append(isolate_move(raw_move_array_bin[i], raw_move_array_bin[i - 1], 'b'))
    compiled_moves_dict = {
        'white_rook': np.zeros((8,8)),
        'white_knight': np.zeros((8, 8)),
        'white_bishop': np.zeros((8, 8)),
        'white_king': np.zeros((8, 8)),
        'white_queen': np.zeros((8, 8)),
        'white_pawn': np.zeros((8, 8)),

        'black_rook': np.zeros((8,8)),
        'black_knight': np.zeros((8, 8)),
        'black_bishop': np.zeros((8, 8)),
        'black_king': np.zeros((8, 8)),
        'black_queen': np.zeros((8, 8)),
        'black_pawn': np.zeros((8, 8))
    }

    convert_number_to_piece_name = {
        1: 'white_rook', 2: 'white_knight', 3: 'white_bishop',
        4: 'white_king', 5: 'white_queen', 6: 'white_pawn',

        -1: 'black_rook', -2: 'black_knight', -3: 'black_bishop',
        -4: 'black_king', -5: 'black_queen', -6: 'black_pawn'
    }


    for array in isolated_move_array_bin[move_cutoff:]:
        piece_moved_num = array[np.nonzero(array)]
        if len(piece_moved_num) > 1: #castling moves two pieces
            for num in piece_moved_num:
                num_array = np.copy(array)
                num_array[num_array != num] = 0
                piece_moved = convert_number_to_piece_name[num]
                compiled_moves_dict[piece_moved] += num_array/num

        # normal move
        else:
            piece_moved = convert_number_to_piece_name[piece_moved_num[0]]
            compiled_moves_dict[piece_moved] += array/piece_moved_num[0]  # need to divide arrays by their number at end of combination

    return compiled_moves_dict

import pandas as pd

columns = ['game_id', 'result', "white_elo", 'black_elo', 'white_rating_diff',
           'black_rating_diff', 'eco', 'opening', 'time_control', 'all_game_moves']
df = pd.read_csv('/media/zackstrater/New Volume/chess_data/white_wins_full_game_lichess_data_jan_2021_cleaned',
                 names=columns)

df2 = df[df['opening'] == 'Ruy Lopez']
total_heat_map = {
        'white_rook': np.zeros((8,8)),
        'white_knight': np.zeros((8, 8)),
        'white_bishop': np.zeros((8, 8)),
        'white_king': np.zeros((8, 8)),
        'white_queen': np.zeros((8, 8)),
        'white_pawn': np.zeros((8, 8)),

        'black_rook': np.zeros((8,8)),
        'black_knight': np.zeros((8, 8)),
        'black_bishop': np.zeros((8, 8)),
        'black_king': np.zeros((8, 8)),
        'black_queen': np.zeros((8, 8)),
        'black_pawn': np.zeros((8, 8))
    }
for game in df2['all_game_moves']:
    moves = game.split(' ')
    game_heat_map_dict = compile_moves(moves[:-1], move_cutoff=5)
    for k,v in game_heat_map_dict.items():
        total_heat_map[k] += v

import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
data = total_heat_map['black_king']

ax = sns.heatmap(data)
plt.show()

