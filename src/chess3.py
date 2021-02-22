import chess
import chess.engine


board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci("/home/zackstrater/stockfish_13_linux_x64_bmi2/stockfish_13_linux_x64_bmi2")

def stockfish_evaluation(board, engine, depth = 20):
    result = engine.analyse(board, chess.engine.Limit(depth=depth))
    return result['score']


print(board.fen())
print(stockfish_evaluation(board, engine))

board.push_san('d4')
print(board.fen())
print(stockfish_evaluation(board, engine))

board.push_san('Nf6')
print(board.fen())
print(stockfish_evaluation(board, engine))

board.push_san('c4')
print(board.fen())
print(stockfish_evaluation(board, engine))

board.push_san('d6')
print(board.fen())
print(stockfish_evaluation(board, engine))

board.push_san('Nc3')
print(board.fen())
print(stockfish_evaluation(board, engine))

board.push_san('g6')
print(board.fen())
print(stockfish_evaluation(board, engine))


engine.quit()