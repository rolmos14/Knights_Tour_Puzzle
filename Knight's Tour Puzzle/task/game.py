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
        # Initialize starting and current position
        self.start_pos_x, self.start_pos_y = [0, 0]
        self.curr_pos_x, self.curr_pos_y = [0, 0]

    def run_game(self):
        self.start_position()
        if self.play_game():
            if self.has_solution():
                # Clean generated solution
                self.reset_valid_moves()
                # Mark starting position as "X"
                self.board[self.start_pos_y][self.start_pos_x] = "X"
                # Update board with possible moves
                self.update_valid_moves()
                # Print initial board status
                print(self)
                # Player plays the game
                self.player_move()
        elif self.has_solution():
            print("Here's the solution!")
            print(self)

    def start_position(self):
        while True:
            try:
                self.start_pos_x, self.start_pos_y = [int(pos) - 1 for pos in
                                                      input("Enter the knight's starting position: ").split()]
                self.curr_pos_x = self.start_pos_x
                self.curr_pos_y = self.start_pos_y
                if not self.cell_on_board(self.start_pos_x, self.start_pos_y):
                    raise ValueError
                break  # valid position
            except ValueError:
                print("Invalid position!")

    def play_game(self):
        while True:
            play = input("Do you want to try the puzzle? (y/n): ")
            if play == "y":
                return True
            if play == "n":
                return False
            print("Invalid input!")

    def has_solution(self):
        # Step counter for visited cells
        pos = 1
        self.board[self.curr_pos_y][self.curr_pos_x] = str(pos)
        if self.solve_knight_tour(self.curr_pos_x, self.curr_pos_y, pos + 1):
            return True
        else:
            print("No solution exists!")
            return False

    def solve_knight_tour(self, new_x, new_y, pos):
        """
        Recursive function to solve Knight Tour
        """
        # Base case, all cells visited
        if pos > self.columns * self.rows:
            return True
        # Try all next moves from the current position
        for x, y in self.valid_moves:
            target_x = new_x + x
            target_y = new_y + y
            if self.ia_move_is_valid(target_x, target_y):
                # Store position counter in current cell
                self.board[target_y][target_x] = str(pos)
                # Check if there is solution through this path recursively
                if self.solve_knight_tour(target_x, target_y, pos + 1):
                    return True
                # Backtracking, reset position
                self.board[target_y][target_x] = "_"
        return False

    def ia_move_is_valid(self, x, y):
        if 0 <= x < self.columns and 0 <= y < self.rows and self.board[y][x] == "_":
            return True
        return False

    def player_move(self):
        while True:
            try:
                move_x, move_y = [int(pos) - 1 for pos in input("Enter your next move: ").split()]
                if not self.player_move_is_valid(move_x, move_y, move_in_progress=True):
                    raise ValueError
                # Mark the position as visited ("*")
                self.board[self.curr_pos_y][self.curr_pos_x] = "*"
                # Move the knight to new position
                self.curr_pos_x = move_x
                self.curr_pos_y = move_y
                self.board[self.curr_pos_y][self.curr_pos_x] = "X"
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

    def player_move_is_valid(self, pos_x, pos_y, move_in_progress=False):
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

    def reset_valid_moves(self):
        for x in range(self.columns):
            for y in range(self.rows):
                if self.board[y][x].isnumeric():
                    self.board[y][x] = "_"

    def update_valid_moves(self):
        for x, y in self.valid_moves:
            target_x = self.curr_pos_x + x
            target_y = self.curr_pos_y + y
            # Update cell only if it's inside valid dimensions and has not been visited yet
            if self.player_move_is_valid(target_x, target_y):
                self.board[target_y][target_x] = str(self.warnsdorff(target_x, target_y))

    def warnsdorff(self, pos_x, pos_y):
        moves = 0
        for x, y in self.valid_moves:
            target_x = pos_x + x
            target_y = pos_y + y
            # Count target only if it's inside board dimensions and cell has not been visited yet
            if self.player_move_is_valid(target_x, target_y):
                moves += 1
        return moves

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
game.run_game()
