import chess

from PieceSquareTables import pst

value_dict = {
    'p': 1,
    'n': 3,
    'b': 3,
    'r': 5,
    'q': 9,
    'k': 0,
    'none': 0,
}

types = ['p', 'n', 'b', 'r', 'q', 'k']
piece_mapper = {
    'p' : chess.PAWN,
    'n' : chess.KNIGHT,
    'b' : chess.BISHOP,
    'r' : chess.ROOK,
    'q' : chess.QUEEN,
    'k' : chess.KING
}

def piece_diff(board, piece_type):
    return len(board.pieces(piece_type, chess.WHITE)) - len(board.pieces(piece_type, chess.BLACK))

def piece_table_evaluation_function(board):
    difference = 0

    for p in types:
        for piece in board.pieces(piece_mapper[p], chess.WHITE):
            difference += pst[p][piece]
        for piece in board.pieces(piece_mapper[p], chess.BLACK):
            difference -= pst[p][chess.square_mirror(piece)]

    if (board.turn):
        difference *= -1

    return difference

def weighted_points_evaluation_function(board: chess.Board):
    difference = 0

    difference += piece_diff(board, chess.PAWN) * 100.0
    difference += piece_diff(board, chess.KNIGHT) * 300.0
    difference += piece_diff(board, chess.BISHOP) * 300.0
    difference += piece_diff(board, chess.ROOK) * 500.0
    difference += piece_diff(board, chess.QUEEN) * 900.0

    if (board.turn):
        difference *= -1

    return difference

def evaluation_function(board):
    return weighted_points_evaluation_function(board) + piece_table_evaluation_function(board)

INF = 100000000000

class MinimaxAI():
    def __init__(self, index, depth):
        self.depth = depth
        self.index = index

    def choose_move(self, board: chess.Board):
        minimaxScores = []
        legalActions = list(board.legal_moves)

        for move in legalActions:
            board.push(move)
            score = self.minimax(board, self.index, 0)
            board.pop()
            minimaxScores.append((score, move))

        max_move = None
        max_move_value = -INF

        for scoreMove in minimaxScores:
            if (scoreMove[0] > max_move_value):
                max_move_value = scoreMove[0]
                max_move = scoreMove[1]

        return max_move

    def minimax(self, board, maximizingAgent, currentDepth):

        if currentDepth == self.depth:
            return evaluation_function(board)

        if board.is_checkmate() or board.is_stalemate() or board.is_repetition():
            return -100000000 if board.turn == self.index else 100000000

        if currentDepth % 2 == 0:
            return self.min_value(board, self.getOpponentIndex(), currentDepth)
        else:
            return self.max_value(board, maximizingAgent, currentDepth)

    def min_value(self, board, minimizingAgent, depth):
        v = 1000000000000
        moves = list(board.legal_moves)

        for move in moves:
            board.push(move)
            v = min(v, self.minimax(board, minimizingAgent, depth + 1))
            board.pop()

        return v

    def max_value(self, board, maximizingAgent, depth):
        v = -1000000000000
        moves = list(board.legal_moves)

        for move in moves:
            board.push(move)
            v = max(v, self.minimax(board, maximizingAgent, depth + 1))
            board.pop()

        return v

    def getOpponentIndex(self):
        return chess.COLORS[1 - chess.COLORS.index(self.index)]