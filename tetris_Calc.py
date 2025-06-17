import time
import os

# Constants
WIDTH, HEIGHT = 10, 20
EMPTY = 0
BLOCK = 1

# Initialize the grid (empty space)
grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Define the Tetriminos as 4x4 matrices
tetriminos = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]]
}

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the grid
def print_grid():
    for row in grid:
        print("".join(["#" if cell == BLOCK else "." for cell in row]))

# Function to check if a piece can be placed
def valid_move(tetromino, offset_x, offset_y):
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell:
                grid_x = x + offset_x
                grid_y = y + offset_y
                if grid_x < 0 or grid_x >= WIDTH or grid_y >= HEIGHT or grid[grid_y][grid_x]:
                    return False
    return True

# Function to place a tetrimino on the grid
def place_tetromino(tetromino, offset_x, offset_y):
    for y, row in enumerate(tetromino):
        for x, cell in enumerate(row):
            if cell:
                grid[y + offset_y][x + offset_x] = BLOCK

# Function to rotate a tetrimino (90 degrees)
def rotate(tetromino):
    return list(zip(*reversed(tetromino)))

# Function to clear full lines
def clear_lines():
    global grid
    grid = [row for row in grid if any(cell == EMPTY for cell in row)]
    while len(grid) < HEIGHT:
        grid.insert(0, [EMPTY] * WIDTH)

# Main Game Loop
def game():
    tetromino_key = 'T'  # Randomize this
    tetromino = tetriminos[tetromino_key]
    offset_x, offset_y = WIDTH // 2 - len(tetromino[0]) // 2, 0
    game_over = False

    while not game_over:
        clear()
        print_grid()
        
        # Move down every second (this is just a simple timing mechanism)
        time.sleep(0.5)
        
        # Check if the current position is valid
        if valid_move(tetromino, offset_x, offset_y + 1):
            offset_y += 1
        else:
            # Place the tetrimino
            place_tetromino(tetromino, offset_x, offset_y)
            clear_lines()
            # Reset the piece
            tetromino = tetriminos[tetromino_key]
            offset_x, offset_y = WIDTH // 2 - len(tetromino[0]) // 2, 0

            # Check if the new piece collides immediately (game over condition)
            if not valid_move(tetromino, offset_x, offset_y):
                game_over = True

# Start the game
game()
