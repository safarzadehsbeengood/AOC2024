import sys
from collections import deque
import heapq

with open(sys.argv[1]) as f:
    text = f.read()
    grid = [[*line] for line in text.splitlines()]

    m = len(grid)
    n = len(grid[0])

    start = tuple()
    end = tuple()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j,)
            if grid[i][j] == 'E':
                end = (i, j,)
    si, sj = start
    ei, ej = end

    # (cost, row, col, row direction, col direction)
    pqueue = [(0, si, sj, 0, 1)]

    # (row, col, row dir, col dir)
    seen = {(si, sj, 0, 1)}

    # do a bfs with a priority queue for djikstra's alg
    while pqueue:
        # get cheapest option in graph that has not been seen
        cost, i, j, di, dj = heapq.heappop(pqueue)
        seen.add((i, j, di, dj,))
        if grid[i][j] == 'E':
            print(cost)
            break

        # check all directions
        for newcost, ni, nj, ndi, ndj in [(cost+1, i+di, j+dj, di, dj), (cost + 1000, i, j, dj, -di), (cost + 1000, i, j, -dj, di)]:
            if grid[ni][nj] == '#': continue
            if (ni, nj, ndi, ndj) in seen: continue
            heapq.heappush(pqueue, (newcost, ni, nj, ndi, ndj))
            



