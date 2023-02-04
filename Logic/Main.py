import Board

chess_board = Board.Board()
checkmate = False

def generate_players():
    players = ["white", "black"]
    while True:
        for i in players:
            yield i

if __name__ == "__main__":
    players = generate_players()

    while not checkmate:
        player = next(players)
        fen_board = chess_board.fen()


