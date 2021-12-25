class KnightsTourPuzzle:

    def __init__(self):
        # Initialize empty 8x8 board
        empty_row = ["_" for _ in range(8)]
        self.board = [empty_row.copy() for _ in range(8)]
        # Initialize starting position
        self.start_pos_x, self.start_pos_y = [0, 0]

    def start_game(self):
        try:
            self.start_pos_x, self.start_pos_y = [int(pos) for pos in
                                                  input("Enter the knight's starting position: ").split()]
            if self.start_pos_x not in range(1, 9) or self.start_pos_y not in range(1, 9):
                raise ValueError
            # Mark starting position as "X"
            self.board[self.start_pos_y - 1][self.start_pos_x - 1] = "X"
            # Print current status of the game
            print(self)
        except ValueError:
            print("Invalid dimensions!")

    def __str__(self):
        horizontal_frame = " " + "-" * 19
        board_str = horizontal_frame + "\n"
        for row in range(len(self.board), 0, -1):
            board_str += str(row) + "| " + " ".join(self.board[row - 1]) + " |\n"
        board_str += horizontal_frame + "\n"
        board_str += " " * 3 + " ".join([str(column) for column in range(1, 9)]) + " " * 2
        return board_str


game = KnightsTourPuzzle()
game.start_game()
