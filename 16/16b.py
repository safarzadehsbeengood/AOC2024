import sys
import heapq
from collections import deque

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
    lc = {(si, sj, 0, 1): 0}
    bt = {}
    bc = float("inf")
    es = set()

    while pqueue:
        cost, i, j, di, dj = heapq.heappop(pqueue)
        if cost > lc.get((i, j, di, dj), float("inf")): continue
        lc[(i, j, di, dj)] = cost
        if grid[i][j] == 'E':
            if cost > bc: break
            bc = cost
            es.add((i, j, di, dj))

        for newcost, ni, nj, ndi, ndj in [(cost+1, i+di, j+dj, di, dj), (cost + 1000, i, j, dj, -di), (cost + 1000, i, j, -dj, di)]:
            if grid[ni][nj] == '#': continue
            l = lc.get((ni, nj, ndi, ndj), float("inf"))
            if newcost > l: continue
            if newcost < l:
                bt[(ni,nj,ndi,ndj)] = set()
                lc[(ni,nj,ndi,ndj)] = newcost
            bt[(ni,nj,ndi,ndj)].add((i,j,di,dj))
            heapq.heappush(pqueue, (newcost, ni, nj, ndi, ndj))
            

    print(es)
    seen = set(es)
    queue = deque(es)
    while queue:
        state = queue.popleft()
        for s in bt.get(state, []):
            if s in seen: continue
            seen.add(s)
            queue.append(s)

    print(len({(i, j) for i, j, _, _ in seen}))



