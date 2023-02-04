import Board

BOARD_SIZE = 8
chess_board = Board.Board(BOARD_SIZE)
checkmate = False
#players = ["white", "black"]
turn_counter = 0

def generate_players():
    players = ["white", "black"]
    while True:
        for i in players:
            yield i


def set_board():
    starting_coords = []

    for i in range(32):
        x = i - ((i // BOARD_SIZE) * BOARD_SIZE)
        y = i // BOARD_SIZE
        if i > 15 : y += 4
        starting_coords.append((x, y))

    for i in range(len(starting_coords)):
        if i in [0, 7, 24, 31]:
            chess_board.modify(starting_coords[i], "castle")
        if i in [1, 6, 25, 30]:
            chess_board.modify(starting_coords[i], "knight")
        if i in [2, 5, 26, 29]:
            chess_board.modify(starting_coords[i], "bishop")
        if i in [3, 27]:
            chess_board.modify(starting_coords[i], "queen")
        if i in [4, 28]:
            chess_board.modify(starting_coords[i], "king")
        if 8 <= i < 16 or 16 <= i < 24:
            chess_board.modify(starting_coords[i], "pawn")

    print(chess_board.board_dict)

set_board()

def check_check(b_dict, t_count):
    king_stats = []
    w_piece_stats = []
    b_piece_stats = []
    check = (False, "none")
    for piece in b_dict.items():
        if piece[1][0] == "king":
            king_stats.append(piece)
        elif piece[1][0] != "empty" and piece[1][1] == "white":
            w_piece_stats.append(piece)
        elif piece[1][0] != "empty" and piece[1][1] == "black":
            b_piece_stats.append(piece)
    for king in king_stats:
       if king[1][1] == "black":
            for w_piece in w_piece_stats:
                if chess_board.moving_pieces(w_piece[0], king[0], "white", t_count, "check_check"):
                    if checkmate_check(king, w_piece_stats, b_dict, t_count):
                        print("checkmate!, white wins")
                    else:
                        print("You are in check")
       if king[1][1] == "white":
            for b_piece in b_piece_stats:
                if chess_board.moving_pieces(b_piece[0], king[0], "black", t_count, "check_check"):
                    if checkmate_check(king, b_piece_stats, b_dict):
                        print("checkmate!, black wins")
                    else:
                        print("You are in check")


def checkmate_check(king, opposite_side, b_dict, t_count):
    checkmate_coords = []
    all_confirmed = True
    all_confirmed_list = []
    trueorfalse = []
    kx, ky = king[0]

    for ty in [-1, 0, 1]:
        for tx in [-1, 0, 1]:
            if (tx, ty) == (0, 0):
                continue
            if b_dict.get((kx + tx, ky + ty)) is not None:
                if b_dict[(kx + tx, ky + ty)] == "empty":
                    checkmate_coords.append((kx + tx, ky + ty))
    if len(checkmate_coords) > 0:
        for k in checkmate_coords:
            for p in opposite_side:
                if chess_board.moving_pieces(p[0], k, "white", t_count, "check_check"):
                    all_confirmed_list.append(k)
    else:
        all_confirmed = False

    for k in checkmate_coords:
        if k in all_confirmed_list:
            pass
        else:
            all_confirmed = False

    return all_confirmed


if __name__ == "__main__":
    players = generate_players()

    while not checkmate:
        player = next(players)
        print(player)
        chess_board.draw(8)

        check_check(chess_board.board_dict, turn_counter)

        user_cur_x = int(input("current position(x) ")) - 1
        user_cur_y = int(input("current position(y) ")) - 1
        user_des_x = int(input("destination position(x) ")) - 1
        user_des_y = int(input("destination position(y) ")) - 1

        user_cur = (user_cur_x, user_cur_y)
        user_des = (user_des_x, user_des_y)

        chess_board.moving_pieces(user_cur, user_des, player, turn_counter, "move")
        turn_counter += 1 




