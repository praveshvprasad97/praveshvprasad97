"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0    
    for row in board:
        x += row.count(X)
        o += row.count(O)
    if x > o:
        return O
    if o >= x:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                a = (i,j)
                action.add(a)
    return action
            
    
def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possiable_actions = actions(board)
    
    if action not in possiable_actions:
        raise Exception("invaild")
        
    which_player = player(board)
    
    new_board = copy.deepcopy(board)
    
    new_board[action[0]][action[1]] = which_player
    
    return new_board 

def diagonal_lines(board):
    yield from board
    yield [board[i][i] for i in range(len(board))]

def all_lines(board):
    yield from diagonal_lines(board)
    yield from diagonal_lines(list(zip(*reversed(board))))


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for line in all_lines(board):
        if len(set(line)) == 1 and line[0] is not None:
            return line[0]
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    spaces = actions(board)
    
    if win is not None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
            
    if len(spaces) == 0:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    who_won = winner(board)

    if who_won == X:
        return 1
    elif who_won == O:
        return -1
    else:
        return 0

def max_value(board):

    possible = actions(board)

    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in possible:
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    possible = actions(board)

    if terminal(board):
        return utility(board)
    v = math.inf
    for action in possible:
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    current_actions = actions(board)

    if current_player == X:
        v = -math.inf
        best_move = set()
        for action in current_actions:
            f = min_value(result(board, action))
            if f > v:
                v = f
                best_move = action
    else:
        v = math.inf
        best_move = set()
        for action in current_actions:
            f = max_value(result(board, action))
            if f < v:
                v = f
                best_move = action
    return best_move

