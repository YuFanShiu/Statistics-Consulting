import random

def generate_path(maze, N, M):
    path = [(0, 0)]
    maze[(0, 0)] = 2
    x, y = 0, 0
    print("Generating path:")
    
    while (x, y) != (N-1, M-1):
        if x < N-1 and (y == M-1 or random.choice([True, False])):
            x += 1
        elif y < M-1:
            y += 1
        path.append((x, y))
        maze[(x, y)] = 2

    print("Generated path:", path)

def add_obstacles(maze, min_obstacles, N, M):
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze.get((i, j), 0) == 0]
    print(f"Empty cells available for obstacles: {len(empty_cells)}")
    if len(empty_cells) < min_obstacles:
        print(f"Warning: Not enough empty cells to place {min_obstacles} obstacles.")
        return

    obstacles = random.sample(empty_cells, min_obstacles)
    for cell in obstacles:
        maze[cell] = 1
    print(f"Added obstacles at: {obstacles}")

def set_obstacle(maze, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to set an obstacle (row col): ").split())
        if 0 <= i < N and 0 <= j < M:
            if maze.get((i, j), 0) == 2:
                print("Cannot place an obstacle on the path.")
            else:
                maze[(i, j)] = 1
                print(f"Obstacle set at: ({i}, {j})")
        else:
            print("Coordinates out of bounds.")
    except ValueError:
        print("Invalid input. Please enter integer coordinates.")
    except KeyError:
        print("Invalid coordinates.")

def remove_obstacle(maze, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to remove an obstacle (row col): ").split())
        if 0 <= i < N and 0 <= j < M:
            if maze.get((i, j), 0) == 2:
                print("Cannot remove the path.")
            else:
                maze[(i, j)] = 0
                print(f"Obstacle removed at: ({i}, {j})")
        else:
            print("Coordinates out of bounds.")
    except ValueError:
        print("Invalid input. Please enter integer coordinates.")
    except KeyError:
        print("Invalid coordinates.")

def print_maze(maze, N, M):
    print("Current maze state:")
    # Print top boundary
    print('+' + '---+' * M)
    for i in range(N):
        # Print maze row with cells
        print('|', end='')
        for j in range(M):
            if maze.get((i, j), 0) == 0:
                print('   |', end='')
            elif maze.get((i, j), 0) == 1:
                print(' X |', end='')
            else:
                print(' O |', end='')
        print()
        # Print row boundary
        print('+' + '---+' * M)

def read_blueprint(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines):
                print(f"Line {idx}: {line.strip()}")  # Print each line for debugging

            N = (len(lines) + 1) // 2
            M = (len(lines[0].split('+')) - 1) // 2
            maze = {}
            for i in range(N):
                line_index = 2 * i + 1
                if line_index >= len(lines):
                    print(f"Skipping line {line_index}: out of range")
                    continue
                line = lines[line_index]
                cells = line.split('|')[1:-1]
                for j, cell in enumerate(cells):
                    if cell.strip() == 'X':
                        maze[(i, j)] = 1
                    else:
                        maze[(i, j)] = 0

            # Ensure N and M are correctly calculated
            N = len(lines) // 2
            M = len(lines[1].split('|')) - 2

            print(f"Read maze from {filename} with size {N}x{M}")
            return maze, N, M
    except IOError:
        print("File not found. Please enter a valid file name.")
        return None, None, None

def main():
    while True:
        filename = input("Enter the maze blueprint file name: ")
        maze, N, M = read_blueprint(filename)
        if maze is not None:
            break
    
    while True:
        try:
            min_obstacles = int(input(f"Enter the minimum number of obstacles (0-{N*M}): "))
            if 0 <= min_obstacles <= N * M:
                break
            else:
                print(f"Number of obstacles must be between 0 and {N*M}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)

    while True:
        print_maze(maze, N, M)
        print("Options:")
        print("1. Set an obstacle")
        print("2. Remove an obstacle")
        print("3. Exit")
        choice = input("Enter your option: ")
        if choice == '1':
            set_obstacle(maze, N, M)
        elif choice == '2':
            remove_obstacle(maze, N, M)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
