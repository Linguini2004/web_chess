import Board

chess_board = Board.Board()
checkmate = False

def check_valid_move(player, move, board):
    chess_board = Board.Board()
    chess_board.load_from_fenstring(board)

    return chess_board.check_move(move, player)
    # True of False

def check_for_check(board):
    chess_board = Board.Board()
    chess_board.load_from_fenstring(board)

    return chess_board.check_for_check()
    # True or False, player in check, piece causing check

def check_mate_brute_force(board):
    chess_board = Board.Board()
    chess_board.load_from_fenstring(board)

    return chess_board.check_mate_brute()
    # True or False, player in checkmate



