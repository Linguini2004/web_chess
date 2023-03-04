import Rules
import ast


class Board():
    board_dict = {}

    def __init__(self):
        with open("initial_state.txt") as f:
            self.board_dict = ast.literal_eval(f.read())

        self.check = None

    def load_from_fenstring(self, fen_string):
        board_state = {}
        piece_ref = {"r": "rook", "n": "knight", "b": "bishop", "k": "king", "q": "queen", "p": "pawn"}

        rows = fen_string.split("/")
        x = y = 0
        for y, row in enumerate(rows):
            for value in row:
                if value.isnumeric():
                    for i in range(int(value)):
                        board_state[(x, y)] = 'empty'
                        x += 1
                else:
                    piece = piece_ref[value.lower()]
                    if value.isupper():
                        player = "white"
                    else:
                        player = "black"
                    board_state[(x, y)] = (piece, player)
                    x += 1
            y += 1
            x = 0

        self.board_dict = board_state

    def generate_fenstring(self, player):
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
            piece, color = self.board_dict[tuple(start_pos)]
        except ValueError:
            return False

        if color != player:
            return False

        if getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[0]:
            return True

    def check_for_check(self):
        kings = [p for p in self.board_dict.items() if p[1][0] == "king"]
        final_pos = [9, 9]
        self.check = None
        for king in kings:
            start_pos = list(king[0][0])
            player = king[1][1]
            paths = []
            for piece in ["rook", "bishop", "knight", "queen", "king", "pawn"]:
                paths = getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[1]
                for cell in paths:
                    occupant = self.board_dict[tuple(cell)]
                    if occupant != "empty":
                        if occupant[0] == piece and occupant[1] != player:
                            self.check = player

                            return True, self.check

        return False, None







