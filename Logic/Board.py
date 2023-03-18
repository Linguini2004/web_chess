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
            print("empty cell")
            return False

        if color != player:
            print("not the same player")
            return False

        '''

        if not self.check_for_check()[0]:
            #("starting out of check")
            if getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[0]:
                self.move_piece(start_pos, final_pos)
                check, affected_player = self.check_for_check()
                #print("check after move", check, affected_player)
                if check and affected_player == player:
                    return False
                else:
                    return True
            else:
                return False

        elif self.check_for_check()[0]:
            #print("starting in check")
            if getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[0]:
                self.move_piece(start_pos, final_pos)
                check, affected_player = self.check_for_check()
                #print("check after move", check, affected_player)
                if not check:
                    return True
                elif check and affected_player != player:
                    return True
                else:
                    return False
            else:
                return False
        
        '''

        if getattr(Rules, piece)(start_pos, final_pos, self.board_dict, player)[0]:
            self.move_piece(start_pos, final_pos)
            check, affected_player = self.check_for_check()
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
                            self.check = player

                            return True, self.check

        return False, None


    def check_for_checkmate(self):
        # if check in the king's current cell
        # we need to check two things
        # first we need to check if the king himself can move out of check
        # This will involve retrieving the valid moves that he can make
        # Then checking for check in each of these positions
        # secondly if none of these work

        check, player = self.check_for_check()
        if not check:
            return False, None

        king = [p for p in self.board_dict.items() if p[1][0] == "king" and p[1][1] == player]
        king_pos = list(king[0])

    '''
    def get_adjacent_cells(self):
        pos = [1, 1]
        adjacent_cells = []

        for i in list():
        if abs(c.x_coord - x_coord) == 1 or abs(c.y_coord - y_coord) == 1:
            result.append(c)
    '''





