import numpy as np

def knight(start_pos, final_pos, board, player):
    moveset = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    paths = pathfind(start_pos, board, moveset, player, 1)

    if final_pos in paths:
        return True, None
    else:
        return False, paths

def pawn(start_pos, final_pos, board, player):
    range = 1

    if player == "black":
        open_moveset = [[0, 1]]
        take_moveset = [[1, 1], [-1, 1]]
        if start_pos[1] == 1:
            range = 2

    elif player == "white":
        open_moveset = [[0, -1]]
        take_moveset = [[1, -1], [-1, -1]]
        if start_pos[1] == 6:
            range = 2

    open_moves = pathfind(start_pos, board, open_moveset, player, range, True, False)
    take_moves = pathfind(start_pos, board, take_moveset, player, 1, False, True)

    if final_pos in open_moves or final_pos in take_moves:
        return True, None
    else:
        return False, take_moves

def rook(start_pos, final_pos, board, player):
    moveset = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    paths = pathfind(start_pos, board, moveset, player)

    if final_pos in paths:
        return True, None
    else:
        return False, paths

def bishop(start_pos, final_pos, board, player):
    moveset = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    paths = pathfind(start_pos, board, moveset, player)

    if final_pos in paths:
        return True, None
    else:
        return False, paths

def queen(start_pos, final_pos, board, player):
    moveset = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]

    paths = pathfind(start_pos, board, moveset, player)

    if final_pos in paths:
        return True, None
    else:
        return False, paths

def king(start_pos, final_pos, board, player):
    moveset = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]

    paths = pathfind(start_pos, board, moveset, player, 1)

    if final_pos in paths:
        return True, None
    else:
        return False, paths

def pathfind(start_pos, board, moveset, player, max_radius=10, open_only=False, take_only=False):
    valid_positions = []
    start_radius = max_radius
    moveset = [np.array(m) for m in moveset]

    for v in moveset:
        pathfound = False
        max_radius = start_radius
        check_pos = np.array(start_pos)
        while not pathfound and max_radius > 0:
            check_pos = np.add(check_pos, v)
            if check_cell(check_pos, board, player) == "open":
                if not take_only:
                    valid_positions.append(check_pos.tolist())
            elif check_cell(check_pos, board, player) == "enemy":
                if not open_only:
                    valid_positions.append(check_pos.tolist())
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
        if board[tuple(position)] == "empty":
            return "open"
        elif board[tuple(position)][1] == player:
            return "friendly"
        elif board[tuple(position)][1] != player:
            return "enemy"
    else:
        return "off_grid"