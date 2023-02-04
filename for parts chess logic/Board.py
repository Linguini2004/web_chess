'''This python file is primarily for creating and modifying the board'''

import Rules

class Board():
    board_dict = {}
    test3 = False

    def __init__(self, board_size):
        for i in range(board_size ** 2):
            self.board_dict[(i - ((i // board_size) * board_size), i // board_size)] = "empty"

    def moving_pieces(self, current, destination, player, turn_num, reason):
        try:
            piece, colour = self.board_dict[current]
        except ValueError:
            print("Sorry, that cell is empty")
            return None

        move_data = current, destination, turn_num, self.board_dict, player
        if self.board_dict[current][1] != self.board_dict[destination][1]:
            rule_check = getattr(Rules, piece)(move_data)
            if reason == "check_check":
                return rule_check
            if reason == "move":
                if rule_check == True:
                    print("That is a valid move")
                    self.board_dict[current] = "empty"
                    self.board_dict[destination] = piece, colour

                else:
                    print("Sorry, I'm afraid that move is invalid!")
        else:
            print("Sorry, that space is occupied by your own %s" % self.board_dict[destination][0])



    def modify(self, coord, to_become):
        x, y = coord
        if y < 4: team = "white"
        else: team = "black"

        self.board_dict[coord] = to_become, team

    def view_board(self):
        return self.board_dict

    def draw(self, size):
        line = []
        list_to_draw = []
        for i in range(0, 9):
            if i == 0:
                list_to_draw.append(" ")
            else:
                list_to_draw.append(str(i))
        for i in self.board_dict.values():
            list_to_draw.append(i)
        for n, i in enumerate(list_to_draw):
            if i == "empty":
                i = " "
            i = i[0]
            line.append(i[0])
            if len(line) == size + 1:
                print(line)
                line.clear()
                line.append(str((n // 9) + 1))

