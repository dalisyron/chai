# pip3 install python-chess


import chess
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys

player1 = AlphaBetaAI(chess.WHITE, 3)
player2 = AlphaBetaAI(chess.BLACK, 3)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    print(game.board.is_checkmate(), game.board.is_stalemate(), game.board.is_repetition())
    game.make_move()


#print(hash(str(game.board)))
