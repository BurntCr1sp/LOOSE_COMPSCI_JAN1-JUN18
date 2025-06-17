import random
import sys
import time
import os

# Constants
SCREEN_WIDTH = 10
SCREEN_HEIGHT = 20
BLOCK_SIZE = 1  # Text-based version uses only 1x1 characters
FPS = 1  # Slow down the game speed (1 frame per second)
LINE_CLEAR_POINTS = [100, 300, 500, 800]  # Points for clearing 1, 2, 3, and 4 lines

# Define colors (Not needed in text-based version)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
COLORS = [CYAN, BLUE, ORANGE, YELLOW, GREEN, RED, PURPLE]

# Shape templates
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[1, 0, 0], [1, 1, 1]],  # J shape
    [[0, 0, 1], [1, 1, 1]]   # L shape
]

# Initialize board
def init_board():
    return [['.' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]

# Function to draw the board
def draw_board(board, score):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen (works for both Windows and Linux/macOS)
    print(f"Score: {score}")
    for row in board:
        print(' '.join(row))

# Function to check for valid move
def valid_move(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = x + off_x
                new_y = y + off_y
                if new_x < 0 or new_x >= SCREEN_WIDTH or new_y >= SCREEN_HEIGHT:
                    return False
                if new_y >= 0 and board[new_y][new_x] != '.':
                    return False
    return True

# Function to merge the shape into the board
def merge(board, shape, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + off_y][x + off_x] = '#'

# Function to clear full lines
def clear_lines(board):
    new_board = [row for row in board if any(cell == '.' for cell in row)]
    lines_cleared = SCREEN_HEIGHT - len(new_board)
    new_board = [['.' for _ in range(SCREEN_WIDTH)]] * lines_cleared + new_board
    return new_board, lines_cleared

# Function to get a random shape
def get_new_shape():
    return random.choice(SHAPES)

# Function to make the piece fall all the way down
def instant_fall(board, shape, offset_x, offset_y):
    while valid_move(board, shape, (offset_x, offset_y + 1)):
        offset_y += 1
    return offset_y

# Main game function
def game():
    board = init_board()
    score = 0
    game_over = False

    # Initial piece
    current_shape = get_new_shape()
    shape_x, shape_y = SCREEN_WIDTH // 2 - len(current_shape[0]) // 2, 0

    while not game_over:
        draw_board(board, score)

        # Event handling (simplified for text-based version)
        print("\nMove your piece: w=up, a=left, s=down, d=right, q=quit")
        move = input().strip().lower()

        # Handle input
        if move == 'q':
            print("Game Over!")
            game_over = True
        elif move == 'a':
            if valid_move(board, current_shape, (shape_x - 1, shape_y)):
                shape_x -= 1
        elif move == 'd':
            if valid_move(board, current_shape, (shape_x + 1, shape_y)):
                shape_x += 1
        elif move == 's':
            # Instant drop
            shape_y = instant_fall(board, current_shape, shape_x, shape_y)
        elif move == 'w':
            # Rotate shape
            rotated_shape = list(zip(*reversed(current_shape)))
            if valid_move(board, rotated_shape, (shape_x, shape_y)):
                current_shape = rotated_shape

        # Handle automatic drop
        if valid_move(board, current_shape, (shape_x, shape_y + 1)):
            shape_y += 1
        else:
            merge(board, current_shape, (shape_x, shape_y))
            board, lines_cleared = clear_lines(board)
            score += LINE_CLEAR_POINTS[min(lines_cleared, 4) - 1]
            current_shape = get_new_shape()
            shape_x, shape_y = SCREEN_WIDTH // 2 - len(current_shape[0]) // 2, 0

            # Check for game over
            if not valid_move(board, current_shape, (shape_x, shape_y)):
                game_over = True

        time.sleep(1)  # Slow down the game speed

# Start the game
if __name__ == "__main__":
    game()
