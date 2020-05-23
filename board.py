import random
import copy
from btnode import Node
from btree import BinaryTree 

class NotEmpty(BaseException):
    pass

class IncorrectCoordinates(BaseException):
    pass

class Board:
    ZER0 = -1
    CROSS = 1
    EMPTY = 0
    DRAW = 2

    def __init__(self):
        self._board = [[0, 0, 0] for i in range(3)]
        self._symbol = Board.CROSS
        self.winning_comb = self.check_winning_combinations()

    def __str__(self):
        s = ''
        for row in self._board:
            for el in row:
                if el == 1:
                    s += 'X' + ' '
                elif el == -1:
                    s += 'O' + ' '
                else:
                    s += '_' + ' '
            s += '\n'
        return s

    def check_winning_combinations(self):
        winning_combinations = list()
        for i in range(3):
            combination_1 = list()
            combination_2 = list()
            for j in range(3):
                combination_1.append((i, j))
                combination_2.append((j, i))
            winning_combinations.append(combination_1)
            winning_combinations.append(combination_2)

        combination_3 = [(0, 0), (1, 1), (2, 2)]
        combination_4 = [(0, 2), (1, 1), (2, 0)]

        winning_combinations.append(combination_3)
        winning_combinations.append(combination_4)
        
        return winning_combinations
    
    def empty_cells(self):
        empty_cells = list()
        for i in range(3):
            for j in range(3):
                if self._board[i][j] == Board.EMPTY:
                    empty_cells.append((i,j))
            
        return empty_cells

    def check_current_table(self):
        comb = self.winning_comb
        for i in range(len(comb)):
            if self._board[comb[i][0][0]][comb[i][0][1]] == self._board[comb[i][1][0]][comb[i][1][1]] == self._board[comb[i][2][0]][comb[i][2][1]]:
                if self._board[comb[i][0][0]][comb[i][0][1]] != Board.EMPTY:
                    return self._board[comb[i][0][0]][comb[i][0][1]]

        if len(self.empty_cells()) == 0:
            return Board.DRAW

        return Board.EMPTY

    def move_random(self):
        cells_to_use = self.empty_cells()
        move = random.choice(cells_to_use)
        self._board[move[0]][move[1]] = self._symbol
        self._symbol *= -1
        return self

    def user_move(self, row, col):
        if row < 0 or row > 2:
            raise IncorrectCoordinates
        if col < 0 or col > 2:
            raise IncorrectCoordinates
        if self._board[row][col] != Board.EMPTY:
            raise NotEmpty
        else:
            self._board[row][col] = self._symbol
            self._symbol *= -1

    def winning_count(self):
        end_of_game = self.check_current_table()
        if end_of_game:
            if  end_of_game == 1:
                return 1
            else: 
                return 0

        node = Node(self)
        tree = BinaryTree(node)
        left_board = copy.deepcopy(self)
        right_board = copy.deepcopy(self)
        left_move = left_board.move_random()
        right_move = right_board.move_random()
        
        tree._root.left = Node(left_move)
        tree._root.right = Node(right_move)
        return left_board.winning_count() + right_board.winning_count()

