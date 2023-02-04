import Rules
import ast


class Board():
    board_dict = {}

    def __init__(self):
        with open("initial_state.txt") as f:
            self.board_dict = ast.literal_eval(f.read())

    def fen(self):
        fen_list = []
        piece_ref = {"rook": "r", "knight": "n", "bishop": "b", "king": "k", "queen": "q", "pawn": "p"}
        for (x, y), value in self.board_dict.items():
            try:
                cell, player = value
                if player == "white":
                    fen_list.append(piece_ref[cell].upper())
                else:
                    fen_list.append(piece_ref[cell])

            except ValueError:
                if fen_list[-1].isdigit():
                    fen_list[-1] = str(int(fen_list[-1]) + 1)
                else:
                    fen_list.append("1")

            if x == 7 and y != 7:
                fen_list.append("/")

        fen_string = "".join(fen_list)
        print(fen_string)

