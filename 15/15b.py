import sys

with open(sys.argv[1]) as f:
    text = f.read()
    text = text.replace('#', '##')
    text = text.replace('O', '[]')
    text = text.replace('.', '..')
    text = text.replace('@', '@.')
    print(text)

    grid, moves = text.split('\n\n')

    grid = [[*line] for line in grid.splitlines()]

    m = len(grid)
    n = len(grid[0])

    # print(grid)
    moves = moves.replace('\n', '')
    # print(moves)

    # find start
    start = (0, 0,)
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
                grid[i][j] = '.'
                break



    dirs = {
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1),
        '^': (-1, 0)
    }

    i, j = start
    def print_grid():
        for x in range(m):
            for b in range(n):
                if x == i and b == j:
                    print('@', end='')
                    continue
                c = grid[x][b]
                print(c, end='')
            print()
        print()

    def bfs(start, move):
        di, dj = dirs[move]
        queue = [start]
        seen = set()
        seen.add(start)
        i, j = start
        if grid[i][j] == '[':
            queue.append((i, j+1,))
            seen.add((i, j+1,))
        else:
            queue.append((i, j-1,))
            seen.add((i, j-1,))

        while queue:
            curr = queue.pop(0)
            i, j = curr
            seen.add(curr)

            if grid[i][j] == '[' and (i, j+1) not in seen:
                queue.append((i, j+1,))
                seen.add((i, j+1,))
            if grid[i][j] == ']' and (i, j-1,) not in seen:
                queue.append((i, j-1,))
                seen.add((i, j-1,))

            if (grid[i+di][j+dj] == '[' or grid[i+di][j+dj] == ']') and (i+di, j+dj,) not in seen:
                queue.append((i+di, j+dj,))
                seen.add((i+di, j+dj,))
                
        return list(seen)


    for move in moves.strip():
        di, dj = dirs[move]
        # print(move, f'{i+di}, {j+dj}')
        # if a wall in front, continue
        if grid[i+di][j+dj] == '#':
            # print("wall")
            continue
        # if an empty space in front, move there
        elif grid[i+di][j+dj] == '.':
            # print("empty space")
            grid[i+di][j+dj], grid[i][j] = grid[i][j], grid[i+di][j+dj]
            i += di
            j += dj
        else:
            # print("PUSH")
            if move == '<' or move == '>':
                # print("box")
                # find the last box in the chain of boxes in front of the robot
                bi, bj = i+di, j+dj
                while grid[bi][bj] == ']' or grid[bi][bj] == '[':
                    bi += di
                    bj += dj
                # if the last box has a wall in front of it, we can't push the box(es)
                if grid[bi][bj] == '#':
                    continue
                else:
                    if move == '<':
                        grid[i] = grid[i][:bj] + grid[i][bj+1:j+1] + ['.'] + grid[i][j+1:]
                    else:
                        grid[i] = grid[i][:j] + ['.'] + grid[i][j:bj] + grid[i][bj+1:]
                    i += di
                    j += dj
            else:
                to_move = bfs((i+di, j+dj), move)
                if move == '^':
                    to_move.sort(key=lambda x: x[0])
                else:
                    to_move.sort(key=lambda x: x[0], reverse=True)
                blocked = False
                # check if farthest row is blocked
                for be in to_move:
                    bi, bj = be
                    if grid[bi][bj] == '[':
                        oj = bj+1
                    else:
                        oj = bj-1
                    if grid[bi+di][bj] == '#' or grid[bi+di][oj] == '#':
                        blocked = True
                        break
                if not blocked:
                    def swap(ai, aj, ci, cj):
                        # print(f'swap ({ai}, {aj}) <-> ({ci}, {cj})')
                        grid[ai][aj], grid[ci][cj] = grid[ci][cj], grid[ai][aj]

                    for be in to_move:
                        bi, bj = be
                        if move == '^':
                            swap(bi, bj, bi-1, bj)
                        else:
                            swap(bi, bj, bi+1, bj)
                    i += di
                    j += dj
                        # print_grid()

    print_grid()
    pt2 = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '[':
                pt2 += 100 * i +j
                
    print(pt2)

