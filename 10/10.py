import sys

def pretty_print(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=' ')
        print()

with open(sys.argv[1], "r") as f:
    text = f.read().split('\n')[:-1]
    mat = [list(map(int, [*line])) for line in text]
    pretty_print(mat)

    m = len(mat)
    n = len(mat[0])

    starts = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                starts.append((i, j))

    def bfs(start):
        score = 0
        visited = set(start)
        queue = [start]
        i, j = start
        while queue:
            i, j = queue.pop(0)
            # print(i, j)
            if mat[i][j] == 9:
                score += 1
            visited.add((i, j))
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= i + di < m and 0 <= j + dj < n and (i+di, j+dj) not in visited and mat[i+di][j+dj] == mat[i][j] + 1:
                    visited.add((i+di, j+dj))
                    queue.append((i+di, j+dj))
        return score

    dfs_paths = []
    def dfs(current, visited, path):
        visited.add(current)
        i, j = current
        # print(current, mat[i][j])
        if mat[i][j] == 9:
            dfs_paths.append(path)
            return
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 0 <= i + di < m and 0 <= j + dj < n and (i+di, j+dj) not in visited and mat[i+di][j+dj] == mat[i][j] + 1:
                visited.add((i+di, j+dj))
                path.append((i+di, j+dj))
                dfs((i+di, j+dj), visited, path)
                visited.remove((i+di, j+dj))
                path.pop()

    res = 0
    for start in starts:
        res += bfs(start)
    print(res)

    for start in starts:
        visited = set()
        path = [start]
        dfs(start, visited, path)
    print(len(dfs_paths))

    # pretty_print(mat)

