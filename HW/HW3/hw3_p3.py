def print_grid(rows, cols, grid):
    for i in range(rows-1, -1, -1):
        print('-' * cols +" ")
        

def update_grid(grid, row, col, value):
    for i in range(0, row):
        if grid[i][col-1] == '_':
            grid[i][col-1] = value
            return
#n = int(input("enter the size of grid:"))
n = 5
grid = [[' ' for _ in range(n)] for _ in range(n)]



i = 2
j = 3
print_grid(n, n, grid)

update_grid(grid, i, j, "H")

    