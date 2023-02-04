'''This python file contains the rules for the movements of pieces'''

# tuple must include -current -destination -turn_num
def knight(move_data):
    (xc, yc), (xd, yd), turn_num, board_dict, player = move_data
    confirmed = False
    x_diff = abs(xc - xd)
    y_diff = abs(yc - yd)
    if x_diff in [1, 2] and y_diff in [1, 2] and x_diff != y_diff:
        confirmed = True
    return confirmed

def pawn(move_data):
    (xc, yc), (xd, yd), turn_num, board_dict, player = move_data
    confirmed = False
    x_diff = abs(xc - xd)
    y_diff = abs(yc - yd)
    pawn_side_dict = {"white" : 1, "black" : -1}
    if inbetween((xc, yc), (xd, yd), board_dict) and xc == xd:
        if turn_num == 0:
            if (yd - yc) * pawn_side_dict[board_dict[(xc, yc)][1]] in [1, 2]:
                confirmed = True
        else:
            if (yd - yc) * pawn_side_dict[board_dict[(xc, yc)][1]] == 1:
                confirmed = True
    elif board_dict[(xd, yd)][0] != "empty" and board_dict[(xc, yc)][1] != board_dict[(xd, yd)][0] and (yd - yc) * pawn_side_dict[board_dict[(xc, yc)][1]] == 1:
        if x_diff == 1 and y_diff == 1:
            confirmed = True
    return confirmed



def castle(move_data):
    (xc, yc), (xd, yd), turn_num, board_dict, player = move_data
    confirmed = False
    x_diff = abs(xc - xd)
    y_diff = abs(yc - yd)
    if inbetween((xc, yc), (xd, yd), board_dict):
        if x_diff == 0 or y_diff == 0 and x_diff != y_diff:
            confirmed = True
    return confirmed

def bishop(move_data):
    (xc, yc), (xd, yd), turn_num, board_dict, player = move_data
    confirmed = False
    x_diff = abs(xc - xd)
    y_diff = abs(yc - yd)
    if inbetween((xc, yc), (xd, yd), board_dict):
        if x_diff == y_diff:
            confirmed = True
    return confirmed

def queen(move_data):
    confirmed = False
    if castle(move_data) or bishop(move_data):
        confirmed = True
    return confirmed

def king(move_data):
    (xc, yc), (xd, yd), turn_num, board_dict, player = move_data
    x_diff = abs(xc - xd)
    y_diff = abs(yc - yd)
    if x_diff < 2 and y_diff < 2:
        confirmed = True
    return confirmed

def inbetween(current, destination, board_dict):
    xc, yc = current
    xd, yd = destination
    confirmed = False
    if xc != xd and yc == yd:
        all_confirmed = True
        if xd > xc:
            for i in range((xd - xc) - 1):
                if board_dict[(xc + (i + 1), yc)] != "empty": all_confirmed = False
        if xc > xd:
            for i in range((xc - xd) - 1):
                if board_dict[(xc - (i + 1), yc)] != "empty": all_confirmed = False
        if all_confirmed:
            confirmed = True

    if yc != yd and xc == xd:
        all_confirmed = True
        if yd > yc:
            for i in range((yd - yc) - 1):
                if board_dict[(xc, yc + (i + 1))] != "empty": all_confirmed = False
        if yc > yd:
            for i in range((yc - yd) - 1):
                if board_dict[(xc, yc - (i + 1))] != "empty": all_confirmed = False

        if all_confirmed:
            confirmed = True

    if xc != xd and yc != yd and abs(xc-xd) == abs(yc-yd):
        all_confirmed = True
        if xd > xc and yd > yc:
            for i in range((xd - xc) - 1):
                if board_dict[(xc + (i + 1), yc + (i + 1))] != "empty": all_confirmed = False
        if xd > xc and yc > yd:
            for i in range((xd - xc) - 1):
                if board_dict[(xc + (i + 1), yc - (i + 1))] != "empty": all_confirmed = False
        if xc > xd and yc > yd:
            for i in range((xc - xd) - 1):
                if board_dict[(xc - (i + 1), yc - (i + 1))] != "empty": all_confirmed = False
        if xc > xd and yd > yc:
            for i in range((xc - xd) - 1):
                if board_dict[(xc - (i + 1), yc + (i + 1))] != "empty": all_confirmed = False
        if all_confirmed:
            confirmed = True
    return confirmed

'''>>> coords = [(0, x) for x in range(3)]
>>> pieces = [d[c] for c in coords]
>>> all(piece == "empty" for piece in pieces)
'''
