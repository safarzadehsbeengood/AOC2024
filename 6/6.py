import sys
from tqdm import tqdm
def print_visited(mat, pos, visited):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (i, j) in visited: 
                print("O", end='')
            else:
                print(mat[i][j], end='')
        print()
    print()

directions = [(-1, 0),
              (0, 1),
              (1, 0),
              (0, -1)
              ]

with open(sys.argv[1], "r") as f:
    text = f.read().split('\n')[:-1]
    mat = [[*line] for line in text]
    m = len(mat)
    n = len(mat[0])
    txt = ('\n'.join([''.join([el for el in line]) for line in mat]))
    print(txt.count("#"))
    print(f'{m}x{n} = {m*n}')
    start = None
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '^':
                start = (i, j, 0)

    def eval(mat, start):
        direction = 0
        di, dj = directions[start[2]] 
        pos = start
        visited = set()
        while 0 <= pos[0]+di < m and 0 <= pos[1]+dj < n:
            # print_visited(mat, pos, visited)
            # print(pos)
            i, j, direction = pos
            if (pos in visited and mat[i+di][j+dj] in visited) or (pos in visited and mat[i+di][j+dj] == '#'):
                return (True, mat, visited)
            visited.add(pos)
            if mat[i+di][j+dj] == '#':
                pos = (i, j, (direction+1)%4) 
                di, dj = directions[pos[2]]
            else:
                pos = (i + di, j + dj, direction)
        return (False, mat, visited)
    
    res = 0
    with tqdm(total=m*n-txt.count("#")-1) as pbar:
        for i in range(m):
            for j in range(n):
                new_mat = [[*line] for line in text]
                if new_mat[i][j] == "#" or mat[i][j] == "^":
                    continue
                else:
                    new_mat[i][j] = '#'
                    result = eval(new_mat, start)
                    if result[0] == True:
                        # print_visited(new_mat, start, result[2])
                        res += 1
                pbar.update()
        print(res)
