import chess
import chess.engine

stockfish_engine = chess.engine.SimpleEngine.popen_uci("/home/zackstrater/stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")


def stockfish_evaluation(board, engine, eval_time=0.1):
    board_state_evaluation = engine.analyse(board, chess.engine.Limit(time=eval_time))
    return board_state_evaluation['score']

board = chess.Board()
for move in first_ten_moves_current_game:
    board.push_san(move)
eval_at_ten_moves.append(stockfish_evaluation(board, stockfish_engine))


stockfish_engine.quit()

pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)  # or 199
# print(df)