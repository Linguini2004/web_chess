import numpy as np

def knight(start_pos, final_pos, board, player):
    moveset = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    if final_pos in pathfind(start_pos, board, moveset, player, 1):
        return True

def pawn(start_pos, final_pos, board, player):
    range = 1

    if player == "white":
        moveset = [[0, 1]]
        if start_pos[1] == 1:
            range = 2

    elif player == "black":
        moveset = [[0, -1]]
        if start_pos[1] == 6:
            range = 2

    if final_pos in pathfind(start_pos, board, moveset, player, range):
        return True

def rook(start_pos, final_pos, board, player):
    moveset = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    if final_pos in pathfind(start_pos, board, moveset, player):
        return True

def bishop(start_pos, final_pos, board, player):
    moveset = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    if final_pos in pathfind(start_pos, board, moveset, player):
        return True

def queen(start_pos, final_pos, board, player):
    moveset = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]

    if final_pos in pathfind(start_pos, board, moveset, player):
        return True

def king(start_pos, final_pos, board, player):
    moveset = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]

    if final_pos in pathfind(start_pos, board, moveset, player, 1):
        return True

def pathfind(start_pos, board, moveset, player, max_radius=10):
    valid_positions = []
    moveset = [np.array(m) for m in moveset]

    for v in moveset:
        check_pos = np.array(start_pos)
        while not pathfound and max_radius > 0:
            check_pos = np.add(check_pos, v)
            if check_cell(check_pos, board, player) == "open":
                valid_positions.append(check_pos)
            elif check_cell(check_pos, board, player) == "enemy":
                valid_positions.append(check_pos)
                pathfound = True
            elif check_cell(check_pos, board, player) == "friendly":
                pathfound = True
            elif check_cell(check_pos, board, player) == "off_grid":
                pathfound = True

            max_radius -= 1

    return valid_positions

def check_cell(position, board, player):
    position = position.tolist()
    if position in [[x, y] for x in range(8) for y in range(8)]:
        if board[position] == "empty":
            return "open"
        elif board[position][1] == player:
            return "friendly"
        elif board[position][1] != player:
            return "enemy"
    else:
        return "off_grid"