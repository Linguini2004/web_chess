import Rules
import ast

class Board():
    board_dict = {}

    def __init__(self):
        with open("initial_state.txt") as f:
            self.board_dict = ast.literal_eval(f.read())


