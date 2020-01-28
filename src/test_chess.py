# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys

player1 = MinimaxAI(chess.WHITE, 2)
player2 = MinimaxAI(chess.BLACK, 2)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    print(game.board.is_checkmate(), game.board.is_stalemate(), game.board.is_repetition())
    game.make_move()


#print(hash(str(game.board)))
