class KnightsTourPuzzle:

    valid_moves = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

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
                # Update board with possible moves
                self.update_valid_moves()
                print("\nHere are the possible moves:")
                # Print current status of the game
                print(self)
                break  # valid position
            except ValueError:
                print("Invalid position!")

    def update_valid_moves(self):
        for x, y in self.valid_moves:
            target_x = self.start_pos_x - 1 + x
            target_y = self.start_pos_y - 1 + y
            # Update cell only if it's inside valid dimensions
            if target_x in range(0, self.columns) and target_y in range(0, self.rows):
                self.board[target_y][target_x] = "O"

    def __str__(self):
        total_cells = self.columns * self.rows
        cell_size = self.digits_len(total_cells)
        horizontal_frame_tab = " " * self.digits_len(self.rows)
        horizontal_frame = horizontal_frame_tab + "-" * (self.columns * (cell_size + 1) + 3)
        board_str = horizontal_frame + "\n"
        # Board rows
        for row in range(self.rows, 0, -1):
            current_row = [cell * cell_size if cell == "_" else cell for cell in self.board[row - 1]]
            board_str += " " * (self.digits_len(self.rows) - self.digits_len(row)) + \
                         str(row) + "| " + " ".join(current_row) + " |\n"
        board_str += horizontal_frame + "\n"
        column_numbers = [" " * (cell_size - self.digits_len(column)) + str(column)
                          for column in range(1, self.columns + 1)]
        board_str += " " * (self.digits_len(self.rows) + 2) + " ".join(column_numbers) + " " * 2
        return board_str

    def digits_len(self, num):
        return len(str(num))


game = KnightsTourPuzzle()
game.start_game()
