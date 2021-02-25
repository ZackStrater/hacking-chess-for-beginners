import chess
import chess.engine
import numpy as np
print(np.version.version)

chess_dict = {
    'r': 7,
    'n': 8,
    'b': 9,
    'k': 10,
    'q': 11,
    'p': 12,
    'R': 1,
    'N': 2,
    'B': 3,
    'K': 4,
    'Q': 5,
    'P': 6,
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

def isolate_move(current_move_array, previous_move_array):
    difference_array = current_move_array - previous_move_array
    isolated_move = difference_array[difference_array < 0] = 0
    return isolated_move

def compile_moves(moves):
    board = chess.Board()
    moves_bin = []
    for i in range(moves):
        board.push_san(moves[i])
    # sum array to find out what piece was moved
    # castling would count as rook + king




board = chess.Board()


move_0 = convert_board_to_array(board)

board.push_san('e4')

move_1 = convert_board_to_array(board)
white_1 = move_1-move_0
white_1[white_1<0] = 0
print(white_1)

board.push_san('e5')

move_2 = convert_board_to_array(board)
print(move_2-move_1)
black_1[black_1>0] = 0
print(white_1)

board.push_san('d4')

move_3 = convert_board_to_array(board)
print(move_3-move_2)

