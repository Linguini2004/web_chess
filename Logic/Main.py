import Board

chess_board = Board.Board()
checkmate = False

def check_valid_move(player, move, board):
    chess_board = Board.Board()
    chess_board.load_from_fenstring(board)
    if chess_board.check_move(move, player):
        return True
    else:
        return False

'''
def generate_players():
    players = ["white", "black"]
    while True:
        for i in players:
            yield i

if __name__ == "__main__":
    players = generate_players()

    while not checkmate:
        player = next(players)
        # Wait to receive the new board (or move) from websocket as fen string
        # Check the move against the rules
        move = [[1, 1], [1, 2]]
        if chess_board.check_move(move, player):
            #chess_board.move_piece(move)
            pass
        fen_board = chess_board.fen(player)
'''




