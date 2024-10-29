import random


# Initialize the board with mines
def initialize_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)] # this for a size of size * size is set to empty --> ""
 
    mine_positions = set() # this set() is used to store multiple items and what we are storing now is the mines

    # Randomly place mines on the board
    while len(mine_positions) < mines: #this is going to loop through the mine_position till it reaches the desired mine
        row, col = random.randint(0, size - 1), random.randint(0, size - 1) #displays random integer 2D matrix that is random.randint(0, size-1) is going to generate random cordinates of size 0 to size-1 for both row and column
        mine_positions.add((row, col)) # this is going to add the row and col position to the mineposition which will be going to be set() more like arranges
        # the above mine_position since its a set it is going to ignore duplicate values

    for row, col in mine_positions: # we are going to loop through the mine_position and place mine on the board
        board[row][col] = 'M' # we are going to place mine in the board
    
    return board, mine_positions

# Display the board
def display_board(board, reveal=False):  #the reveal will determine with the mines will be displayed or not and is going to print the board for the player
    size = len(board)
    print("\n    " + " ".join([str(i) for i in range(size)])) #this is going to print the numbers of the column at the top of the grid
    print("   " + "---" * size) #this prints a separator line to separate the rows
    for i in range(size):
        row_display = [board[i][j] if reveal or board[i][j] != 'M' else ' ' for j in range(size)]
        print(f"{i} | {' '.join(row_display)} |")
    print("   " + "---" * size)

# Count mines around a cell
def count_adjacent_mines(board, row, col):
    size = len(board)
    count = 0
    for i in range(max(0, row - 1), min(size, row + 2)):
        for j in range(max(0, col - 1), min(size, col + 2)):
            if board[i][j] == 'M':
                count += 1
    return count

# Recursively reveal cells
def reveal_cells(board, player_board, row, col):
    if player_board[row][col] != ' ':
        return

    adjacent_mines = count_adjacent_mines(board, row, col)
    player_board[row][col] = str(adjacent_mines)

    if adjacent_mines == 0:
        for i in range(max(0, row - 1), min(len(board), row + 2)):
            for j in range(max(0, col - 1), min(len(board), col + 2)):
                if player_board[i][j] == ' ':
                    reveal_cells(board, player_board, i, j)

# Main game loop
def play_minesweeper(size=5, mines=5):
    board, mine_positions = initialize_board(size, mines)
    player_board = [[' ' for _ in range(size)] for _ in range(size)]
    revealed_cells = 0
    total_cells = size * size - mines

    while revealed_cells < total_cells:
        display_board(player_board)
        try:
            row, col = map(int, input("Enter row and column to reveal (e.g., 0 1): ").split())
            if (row, col) in mine_positions:
                print("Boom! You hit a mine. Game over!")
                display_board(board, reveal=True)
                return
            if player_board[row][col] == ' ':
                reveal_cells(board, player_board, row, col)
                revealed_cells = sum(row.count(' ') == False for row in player_board)
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    print("Congratulations! You've cleared the board!")
    display_board(board, reveal=True)

# Run the game
play_minesweeper()
