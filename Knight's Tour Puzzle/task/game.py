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
        self.pos_x, self.pos_y = [0, 0]

    def start_game(self):
        # Starting position loop
        while True:
            try:
                self.pos_x, self.pos_y = [int(pos) - 1 for pos in
                                          input("Enter the knight's starting position: ").split()]
                if not self.cell_on_board(self.pos_x, self.pos_y):
                    raise ValueError
                # Mark starting position as "X"
                self.board[self.pos_y][self.pos_x] = "X"
                # Update board with possible moves
                self.update_valid_moves()
                # Print current status of the game
                print(self)
                break  # valid position
            except ValueError:
                print("Invalid position!")
        # Next move loop
        while True:
            try:
                move_x, move_y = [int(pos) - 1 for pos in input("Enter your next move: ").split()]
                if not self.move_is_valid(move_x, move_y, move_in_progress=True):
                    raise ValueError
                # Mark the position as visited ("*")
                self.board[self.pos_y][self.pos_x] = "*"
                # Move the knight to new position
                self.pos_x = move_x
                self.pos_y = move_y
                self.board[self.pos_y][self.pos_x] = "X"
                # Reset valid moves
                self.reset_valid_moves()
                # Update valid moves
                self.update_valid_moves()
                # Print current status of the game
                print(self)
                # Check if game is finished
                if self.game_over():
                    break
            except ValueError:
                print("Invalid move! ", end="")

    def game_over(self):
        visited_cells = 1  # current positions counts as visited
        for x in range(self.columns):
            for y in range(self.rows):
                # Check if there is at least one possible move
                if self.board[y][x].isnumeric():
                    return False
                # Check if cell has been visited
                if self.board[y][x] == "*":
                    visited_cells += 1
        # If board is full of "*" but current position "X", it's a win
        if visited_cells == self.rows * self.columns:
            print("What a great tour! Congratulations!")
        else:  # lose
            print("No more possible moves!", f"Your knight visited {visited_cells} squares!", sep="\n")
        return True

    def reset_valid_moves(self):
        for x in range(self.columns):
            for y in range(self.rows):
                if self.board[y][x].isnumeric():
                    self.board[y][x] = "_"

    def update_valid_moves(self):
        for x, y in self.valid_moves:
            target_x = self.pos_x + x
            target_y = self.pos_y + y
            # Update cell only if it's inside valid dimensions and has not been visited yet
            if self.move_is_valid(target_x, target_y):
                self.board[target_y][target_x] = str(self.warnsdorff(target_x, target_y))

    def warnsdorff(self, pos_x, pos_y):
        moves = 0
        for x, y in self.valid_moves:
            target_x = pos_x + x
            target_y = pos_y + y
            # Count target only if it's inside board dimensions and cell has not been visited yet
            if self.move_is_valid(target_x, target_y):
                moves += 1
        return moves

    def move_is_valid(self, pos_x, pos_y, move_in_progress=False):
        # Check if cell is inside board dimensions
        if not self.cell_on_board(pos_x, pos_y):
            return False
        # Check if cell has not been visited ("_") and if it's a valid target (number)
        if "_" not in self.board[pos_y][pos_x] and not self.board[pos_y][pos_x].isnumeric():
            return False
        # If there is a move in progress, only a target with numeric value is allowed
        if move_in_progress and not self.board[pos_y][pos_x].isnumeric():
            return False
        return True

    def cell_on_board(self, pos_x, pos_y):
        # Check if cell is inside board dimensions
        if pos_x in range(0, self.columns) and pos_y in range(0, self.rows):
            return True
        return False

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
        board_str += " " * (self.digits_len(self.rows) + 2) + " ".join(column_numbers) + " " * 2 + "\n"
        return board_str

    def digits_len(self, num):
        return len(str(num))


game = KnightsTourPuzzle()
game.start_game()
