def find_char(mat, c):
    res = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == c:
                res.append((i, j))
    return res

change_map = {

        "R": (0, 1),
        "D": (1, 0),
        "L": (0, -1),
        "U": (-1, 0),
        "DR": (1, 1),
        "DL": (1, -1),
        "UR": (-1, 1),
        "UL": (-1, -1)

    }

with open("input.txt", "r") as f:
    text = f.read()
    # print(text)
    mat = [[*line] for line in text.splitlines()]
    m, n = len(mat), len(mat[0])

    # pt 1

    def check(start, change):
        i, j = start
        for c in 'XMAS':
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return False
            if mat[i][j] == c:
                i += change[0]
                j += change[1] 
            else:
                return False
        return True

    xs = find_char(mat, 'X')

    occ = 0
    paths = []

    for x in xs:
        for d, change in change_map.items():
            if check(x, change):
                occ += 1
                paths.append((x, d))
    # print(paths)
    print(f'{m} x {n}')
    print(occ)

    # pt 2

    valid = set()
    centers = find_char(mat, 'A')
    mas = 0
    for center in centers:
        i, j = center[0], center[1]
        # center can't be on the edge
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            continue
        corners = [mat[i-1][j-1], mat[i-1][j+1], mat[i+1][j-1], mat[i+1][j+1]]        # filter out any Xs with 'X' or 'A' in them
        tl, tr, bl, br = corners
        if any([c == 'X' or c == 'A' for c in corners]):
            continue
        if corners.count('M') == 2 and corners.count('S') == 2:
            # print(i, j, corners)
            if tl != br:
                valid = valid.union(set([(i, j), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]))
                mas += 1 
        else:
            continue

    for i in range(m):
        for j in range(n):
            if (i, j) in valid:
                print(mat[i][j], end='')
            else:
                print('.', end='')
        print()

    print(mas) 

