import random
import copy
from constants import GRID_SIZE

def init_game(n=4):
    board = [[0] * n for _ in range(n)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty = [(x, y) for x in range(len(board)) for y in range(len(board[x])) if board[x][y] == 0]
    if empty:
        x, y = random.choice(empty)
        board[x][y] = 4 if random.random() < 0.1 else 2

def compress(row):
    return [num for num in row if num != 0]

def merge(row, score):
    new_row = []
    skip = False
    for i in range(len(row)):
        if skip:
            skip = False
            continue
        if i + 1 < len(row) and row[i] == row[i + 1]:
            new_value = row[i] * 2
            new_row.append(new_value)
            score += new_value
            skip = True
        else:
            new_row.append(row[i])
    return new_row, score

def move(board, direction, score):
    n = len(board)
    board_copy = copy.deepcopy(board)
    moved = False

    for i in range(n):
        if direction in ('left', 'right'):
            row = board[i] if direction == 'left' else board[i][::-1]
            row, score = merge(compress(row), score)
            row += [0] * (n - len(row))
            if row != board[i] and direction == 'right':
                row = row[::-1]
            if row != board[i]:
                moved = True
                board[i] = row
        else:
            col = [board[j][i] for j in range(n)]
            col = col if direction == 'up' else col[::-1]
            col, score = merge(compress(col), score)
            col += [0] * (n - len(col))
            if col != [board[j][i] for j in range(n)]:
                moved = True
                if direction == 'down':
                    col = col[::-1]
                for j in range(n):
                    board[j][i] = col[j]

    if moved:
        add_new_tile(board)
    return score

def game_over(board):
    if any(0 in row for row in board):
        return False
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (x < len(board) - 1 and board[x][y] == board[x + 1][y]) or (y < len(board[0]) - 1 and board[x][y] == board[x][y + 1]):
                return False
    return True