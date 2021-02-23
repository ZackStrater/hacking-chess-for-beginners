import chess
import chess.engine


board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("/home/zackstrater/stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")

def stockfish_evaluation(board, engine, depth = 20):
    result = engine.analyse(board, chess.engine.Limit(depth=depth))
    return result['score']


engine.quit()