import Main as logic

fen_string = "rnbqkbnr/p1ppp1pp/8/2Q2p2/3P4/1p3N2/PPP1PPPP/RNB1KB1R"
player = "white"
move = [[0, 7], [1, 5]]

print("valid", logic.check_valid_move(player, move, fen_string))