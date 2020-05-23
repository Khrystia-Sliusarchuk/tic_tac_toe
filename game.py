import random
import copy
from board import Board
from board import NotEmpty
from board import IncorrectCoordinates
from btnode import Node
from btree import BinaryTree 

if __name__ == "__main__":
    board = Board()
    while not board.check_current_table():
        print(board)
        row, col = int(input('Enter row: ')), int(input('Enter column: '))
        
        try: 
            board.user_move(row, col)
            left_board = copy.deepcopy(board)
            right_board = copy.deepcopy(board)
            left_move = left_board.move_random()
            right_move = right_board.move_random()
            if left_move.winning_count() > right_move.winning_count():
                board = left_board
            else:
                board = right_board
        except NotEmpty:
            print("Cell is not empty!")
        except IncorrectCoordinates:
            print("Enter appropriate coordinates!")

    if board.check_current_table() == Board.DRAW:
        print("Draw. GAME OVER!")
    elif board.check_current_table() == Board.CROSS:
        print("The user won. GAME OVER!")
    else:
        print("The computer won. GAME OVER!")

        
    