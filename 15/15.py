import sys

with open(sys.argv[1]) as f:
    text = f.read()

    grid, moves = text.split('\n\n')

    grid = [[*line] for line in grid.splitlines()]

    m = len(grid)
    n = len(grid[0])

    # print(grid)
    moves = moves.replace('\n', '')
    # print(moves)

    # find start
    start = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)


    dirs = {
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '^': (-1, 0)
    }

    def print_grid():
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                print(c, end='')
            print()
        print()

    i, j = start
    # print("start")
    # print_grid()
    for move in moves.strip():
        # print(move, f'{i}, {j}')
        di, dj = dirs[move]
        # if a wall in front, continue
        if grid[i+di][j+dj] == '#':
            # print("wall")
            # print_grid()
            continue
        # if an empty space in front, move there
        if grid[i+di][j+dj] == '.':
            # print("empty space")
            grid[i+di][j+dj], grid[i][j] = grid[i][j], grid[i+di][j+dj]
            i += di
            j += dj
            # print_grid()
            continue
        # elif grid[i+di][j+dj] == 'O':
        else:
            # print("box")
            # find the last box in the chain of boxes in front of the robot
            bi, bj = i+di, j+dj
            while grid[bi][bj] == 'O':
                bi += di
                bj += dj
            # if the last box has a wall in front of it, we can't push the box(es)
            if grid[bi][bj] == '#':
                # print_grid()
                continue
            # otherwise, we can just swap the box in front of the robot with the empty spot
            # in front of the robot 
            else:
                grid[i+di][j+dj], grid[bi][bj] = grid[bi][bj], grid[i+di][j+dj]

            grid[i+di][j+dj], grid[i][j] = grid[i][j], grid[i+di][j+dj]
            i += di
            j += dj
        # print_grid()

    pt1 = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'O':
                pt1 += 100 * i + j
    print(pt1)

