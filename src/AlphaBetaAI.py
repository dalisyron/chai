import chess
from math import inf

from MinimaxAI import weighted_points_evaluation_function, piece_table_evaluation_function

value_dict = {
    'p': 1,
    'n': 3,
    'b': 3,
    'r': 5,
    'q': 9,
    'k': 0,
    'none': 0,
}

def evaluation_function(board):
    return weighted_points_evaluation_function(board) + piece_table_evaluation_function(board)

INF = 100000000000

class AlphaBetaAI():
    def __init__(self, index, depth):
        self.depth = depth
        self.index = index

    def choose_move(self, board: chess.Board):
        minimaxScores = []
        legalActions = list(board.legal_moves)


        alpha = -INF
        beta = INF

        for move in legalActions:
            board.push(move)
            score = self.minimax(board, self.index, 0, alpha, beta)
            board.pop()
            minimaxScores.append((score, move))

        max_move = None
        max_move_value = -INF

        for scoreMove in minimaxScores:
            if (scoreMove[0] > max_move_value):
                max_move_value = scoreMove[0]
                max_move = scoreMove[1]

        return max_move

    def minimax(self, board, maximizingAgent, currentDepth, alpha, beta):

        if currentDepth == self.depth:
            return evaluation_function(board)

        if board.is_checkmate() or board.is_stalemate() or board.is_repetition():
            return -100000000 if board.turn == self.index else 100000000

        if currentDepth % 2 == 0:
            return self.min_value(board, self.getOpponentIndex(), currentDepth, alpha, beta)
        else:
            return self.max_value(board, maximizingAgent, currentDepth, alpha, beta)

    def min_value(self, board, minimizingAgent, depth, alpha, beta):
        v = 1000000000000
        moves = list(board.legal_moves)

        for move in moves:
            board.push(move)
            v = min(v, self.minimax(board, minimizingAgent, depth + 1, alpha, beta))
            board.pop()
            if (v <= alpha):
                return v
            beta = min(beta, v)

        return v

    def max_value(self, board, maximizingAgent, depth, alpha, beta):
        v = -1000000000000
        moves = list(board.legal_moves)

        for move in moves:
            board.push(move)
            v = max(v, self.minimax(board, maximizingAgent, depth + 1, alpha, beta))
            board.pop()
            if (v >= beta):
                return v
            alpha = max(alpha, v)

        return v

    def getOpponentIndex(self):
        return chess.COLORS[1 - chess.COLORS.index(self.index)]
