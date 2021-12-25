class KnightsTourPuzzle:

    def __init__(self):
        # Ask for valid board dimensions
        while True:
            try:
                self.columns, self.rows = [int(pos) for pos in input("Enter your board dimensions: ").split()]
                if self.columns < 1 or self.rows < 1:
                    raise ValueError
                break  # valid dimensions
            except ValueError:
                print("Invalid dimensions!")
        # Initialize empty board based on desired dimensions
        empty_row = ["_" for _ in range(self.columns)]
        self.board = [empty_row.copy() for _ in range(self.rows)]
        # Initialize starting position
        self.start_pos_x, self.start_pos_y = [0, 0]

    def start_game(self):
        # Ask for valid starting position
        while True:
            try:
                self.start_pos_x, self.start_pos_y = [int(pos) for pos in
                                                      input("Enter the knight's starting position: ").split()]
                if self.start_pos_x not in range(1, self.columns + 1) or \
                   self.start_pos_y not in range(1, self.rows + 1):
                    raise ValueError
                # Mark starting position as "X"
                self.board[self.start_pos_y - 1][self.start_pos_x - 1] = "X"
                # Print current status of the game
                print(self)
                break  # valid position
            except ValueError:
                print("Invalid position!")

    def __str__(self):
        total_cells = self.columns * self.rows
        cell_size = len(str(total_cells))
        horizontal_frame_tab = " " * len(str(self.rows))
        horizontal_frame = horizontal_frame_tab + "-" * (self.columns * (cell_size + 1) + 3)
        board_str = horizontal_frame + "\n"
        # Board rows
        for row in range(self.rows, 0, -1):
            current_row = [cell * cell_size if cell != "X" else "_" * (cell_size - 1) + "X"
                           for cell in self.board[row - 1]]
            board_str += " " * (len(str(self.rows)) - len(str(row))) + str(row) + "| " + " ".join(current_row) + " |\n"
        board_str += horizontal_frame + "\n"
        column_numbers = [" " * (cell_size - len(str(column))) + str(column)
                          for column in range(1, self.columns + 1)]
        board_str += " " * (len(str(self.rows)) + 2) + " ".join(column_numbers) + " " * 2
        return board_str


game = KnightsTourPuzzle()
game.start_game()
