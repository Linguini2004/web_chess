import Rules
import ast
import numpy as np

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

    def move_piece(self, start_pos, final_pos):
        start_pos = tuple(start_pos)
        final_pos = tuple(final_pos)
        if self.board_dict[start_pos] != "empty":
            data = self.board_dict[start_pos]
            self.board_dict[start_pos] = "empty"
            self.board_dict[final_pos] = data

    def check_move(self, move, player):
        start_pos, final_pos = move
        try:
            piece, color = self.board_dict[tuple(start_pos)]
        except ValueError:
            return False

        if color != player:
            print("not the same player")
            return False

        if getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[0]:
            previous_board_state = dict(self.board_dict)
            self.move_piece(start_pos, final_pos)
            check, affected_player = self.check_for_check()[:2]
            self.board_dict = previous_board_state
            if affected_player != "invalid_check":
                if check:
                    if affected_player != player:
                        return True
                    elif affected_player == player:
                        return False
                    else:
                        print("something went wrong")
                else:
                    return True
        else:
            return False


    def check_for_check(self):
        kings = [p for p in self.board_dict.items() if p[1][0] == "king"]
        final_pos = [9, 9]
        checking_pieces = {}
        self.check = None
        for king in kings:
            start_pos = list(king[0])
            player = king[1][1]
            paths = []
            for piece in ["rook", "bishop", "knight", "queen", "king", "pawn"]:
                paths = getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[1]
                for cell in paths:
                    occupant = self.board_dict[tuple(cell)]
                    if occupant != "empty":
                        if occupant[0] == piece and occupant[1] != player:
                            if self.check != None:
                                return True, "invalid_check", checking_pieces
                            self.check = player
                            checking_pieces[tuple(cell)] = occupant

        if self.check != None:
            return True, self.check, checking_pieces
        else:
            return False, None, None


    def check_for_checkmate(self):

        # if check in the king's current cell
        # we need to check two things
        # first we need to check if the king himself can move out of check
        # This will involve retrieving the valid moves that he can make
        # Then checking for check in each of these positions
        # secondly if none of these work

        check, player, checking_pieces = self.check_for_check()
        if not check:
            return False, None

        king = [p for p in self.board_dict.items() if p[1][0] == "king" and p[1][1] == player]
        king_pos = list(king[0])

        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                pass

        adjacent_squares = [[king_pos[0]+x, king_pos[1]+y] for x in (-1, 0, 1) for y in (-1, 0, 1)]
        size = [[x, y] for x in range(8) for y in range(8)]

        for square in adjacent_squares:
            if square in size:
                if self.check_move([king_pos, square], player):
                    return False

        # ... if we get this far we need to check if another piece can intervene
        # This includes moving into the path of the checking piece or taking the checking piece
        # However we will need to check in the event that there are mutliple checking pieces
        # Can there even be multiple checking pieces?
        # Apparently there can
        # So we will need to retrieve the pieces currently checking the king and their lists of moves between them and the king
        # This part may be slightly harder
        # Once we've passed the checking pieces onto this function we'll need to check the cells inbetween the piece and the king

        for piece in checking_pieces.items():
            king_vect = np.array(king_pos)
            piece_vect = np.array(piece.items[0])
            direction = np.subtract(king_vect, piece_vect)


        # Note it might be cleaner to do this from Rules and have a loop that selects the direction used once the king's position is found withing the valid moves of the checking piece


    def check_mate_brute(self):

        check, player, checking_pieces = self.check_for_check()
        if not check:
            return False, None

        player_pieces = [piece for piece in self.board_dict.items() if piece[1][1] == player]
        board_cells = [[x,y] for x in range(8) for y in range(8)]
        for piece in player_pieces:
            for destination in board_cells:
                if self.check_move([piece[0], destination], player):
                    return False

        return True






