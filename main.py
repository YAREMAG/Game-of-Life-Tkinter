import tkinter as tk
import time
import random

# Declare constants
WIN_W = 520
WIN_H = 520
CELL_W = 40
GRIDSIZE = int(WIN_W/CELL_W)-2
gridsize = 10

# Create grid of size ‘gridsize’
def initial_grid(gridsize):
    grid = []
    for _ in range(gridsize+2):
        grid.append([0 for _ in range(gridsize+2)])
    return grid

# Assign random values (0, 1) to grid
def set_grid_state(grid):
    for row in range(1, len(grid)-1):
        grid[row][1:-1] = [random.randrange(2) for _ in range(len(grid)-2)]
    return grid

# Initialize cells and neighbors
cells = set_grid_state(initial_grid(gridsize))
neighbors = initial_grid(gridsize)

# Create window
window = tk.Tk()
window.title('Game of Life ')

# Create canvas
canvas = tk.Canvas(window, width=WIN_W, height=WIN_H)
canvas.pack()

# Main GOL loop
while True:
    # Clear canvas
    canvas.delete('all')

    # Display current state of cells
    for row in range(1, GRIDSIZE):
        for col in range(1, GRIDSIZE):
            cell_color = 'orange' if cells[row][col] == 1 else 'white'
            canvas.create_rectangle(CELL_W*col, CELL_W*row, CELL_W+(CELL_W*col), CELL_W+(CELL_W*row), fill=cell_color)
    # Update window and pause
    window.update()
    canvas.pack()
    time.sleep(1)

    # Count live neighbors
    for row in range(1, gridsize+1):
        for col in range(1, gridsize+1):
            ncount = 0
            for x in range(-1,2):
                ncount += cells[row+x][col-1:col+2].count(1)
            ncount -= cells[row][col]
            neighbors[row][col] = ncount

    # Apply Conway's GOL rules
    for row in range(1, GRIDSIZE):
        for col in range(1, GRIDSIZE):
            if neighbors[row][col] < 2:
                cells[row][col] = 0
            elif neighbors[row][col] == 3:
                if cells[row][col] == 0:
                    cells[row][col] = 1
            elif neighbors[row][col] > 3:
                cells[row][col] = 0