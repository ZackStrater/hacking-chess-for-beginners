import chess
import chess.engine

stockfish_engine = chess.engine.SimpleEngine.popen_uci("/home/zackstrater/stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")


def stockfish_evaluation(board, engine, eval_time=0.1):
    board_state_evaluation = engine.analyse(board, chess.engine.Limit(time=eval_time))
    return board_state_evaluation['score']

board = chess.Board()
# for move in first_ten_moves_current_game:
#     board.push_san(move)
# eval_at_ten_moves.append(stockfish_evaluation(board, stockfish_engine))
print(board.epd())


stockfish_engine.quit()

# pd.set_option('display.max_columns', None)  # or 1000
# pd.set_option('display.max_rows', None)  # or 1000
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)  # or 199
# # print(df)


class MyChess(chess.Board):

    mapped = {
        'P': 1,     # White Pawn
        'p': -1,    # Black Pawn
        'N': 2,     # White Knight
        'n': -2,    # Black Knight
        'B': 3,     # White Bishop
        'b': -3,    # Black Bishop
        'R': 4,     # White Rook
        'r': -4,    # Black Rook
        'Q': 5,     # White Queen
        'q': -5,    # Black Queen
        'K': 6,     # White King
        'k': -6     # Black King
        }

    def convert_to_int(self):
        epd_string = self.epd()
        list_int = []
        for i in epd_string:
            if i == " ":
                return list_int
            elif i != "/":
                if i in self.mapped:
                    list_int.append(self.mapped[i])
                else:
                    for counter in range(0, int(i)):
                        list_int.append(0)