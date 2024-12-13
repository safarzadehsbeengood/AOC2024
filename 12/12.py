import sys

with open(sys.argv[1]) as f:
    text = f.read()
    plants = set([c for c in set(text) if c != '\n'])
    garden = [[*row] for row in text.splitlines()]

    areas = {c: [] for c in plants}
    perimeters = {c: [] for c in plants}

    m = len(garden)
    n = len(garden[0])

    def neighbors(i, j, plant):
        ct = 0
        if i > 0 and garden[i-1][j] == plant:
            ct += 1
        if i < m-1 and garden[i+1][j] == plant:
            ct += 1
        if j > 0 and garden[i][j-1] == plant:
            ct += 1
        if j < n-1 and garden[i][j+1] == plant:
            ct += 1
        return ct

    global_seen = set()

    edges = {plant: set() for plant in plants}

    def bfs(start):
        global global_seen, areas, perimeters, spots
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        seen = set()
        seen.add(start)
        queue = [start]
        plant = garden[start[0]][start[1]]
        while queue:
            i, j = queue.pop(0)
            seen.add((i, j,))
            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n and (i+di, j+dj) not in seen and garden[i+di][j+dj] == plant:
                    seen.add((i+di, j+dj))
                    queue.append((i+di, j+dj))
                else:
                    edges[plant].add((i, j, di, dj))
        
        global_seen = global_seen.union(seen)
        perimeter = 0
        for i, j in seen:
            perimeter += 4 - neighbors(i, j, plant)
        perimeters[plant].append(perimeter)
        areas[plant].append(len(seen))


    for i in range(m):
        for j in range(n):
            if (i, j) in global_seen:
                continue
            else:
                bfs((i, j))

    pt1 = 0
    for plant in plants:
        A = areas[plant]
        P = perimeters[plant]
        if len(A) != len(P):
            raise ValueError
        for i in range(len(A)):
            pt1 += A[i]*P[i]
        
    print(pt1)

    print(edges)
