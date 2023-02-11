import Rules
import ast


class Board():
    board_dict = {}

    def __init__(self):
        with open("initial_state.txt") as f:
            self.board_dict = ast.literal_eval(f.read())

    def fen(self, player):
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

        fen_list.append(" {}".format(player[0]))
        fen_string = "".join(fen_list)

        return fen_string

    def check_move(self, move, player):
        start_pos, final_pos = move
        try:
            piece, color = self.board_dict[move]
        except ValueError:
            return False

        if color != player:
            return False

        if getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player):
            return True




