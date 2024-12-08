import sys

def pretty_mat(mat: list[list[str]]):
    return '\n'.join([''.join(line) for line in mat])

with open(sys.argv[1]) as f:
    text = f.read()
    print(text)
    mat = [[*line] for line in text.split('\n')][:-1]
    mat_pt2 = mat.copy()
    m = len(mat)
    n = len(mat[0])
    freqs = {}
    for i in range(m):
        for j in range(n):
            if mat[i][j] != '.':
                freq = mat[i][j]
                if freqs.get(freq) != None:
                    freqs[freq].append((i, j))
                else:
                    freqs[freq] = [(i, j)]

    def in_bounds(coord):
        i, j = coord
        if i >= 0 and i < m and j >= 0 and j < n:
            return True
        return False

    def calc_antinodes(a: tuple[int, int], b: tuple[int, int]):
        dist = (a[0]-b[0], a[1]-b[1])
        i, j = dist[0], dist[1]
        a_node, b_node = (a[0]+i, a[1]+j), (b[0]-i, b[1]-j)
        return (a_node if in_bounds(a_node) else False, b_node if in_bounds(b_node) else False)
    
    for freq, coords in freqs.items():
        done = set()
        for a in coords:
            for b in coords:
                if a == b or b in done:
                    continue
                new_nodes = calc_antinodes(a, b)
                if new_nodes[0] != False:
                    i, j = new_nodes[0]
                    mat[i][j] = '#'
                if new_nodes[1] != False:
                    i, j = new_nodes[1]
                    mat[i][j] = '#'
            done.add(a)
    print(pretty_mat(mat))
    print(pretty_mat(mat).count('#'))

    # pt 2


    def calc_antinodes_pt2(a: tuple[int, int], b: tuple[int, int]):
        dist = (a[0]-b[0], a[1]-b[1])
        di, dj = dist[0], dist[1]
        a_antinode = a
        b_antinode = b
        res = []

        while in_bounds(a_antinode):
            i, j = a_antinode
            a_antinode = (i+di, j+dj)
            if not in_bounds(a_antinode):
                break
            res.append(a_antinode)

        while in_bounds(b_antinode):
            i, j = b_antinode
            b_antinode = (i-di, j-dj)
            if not in_bounds(b_antinode):
                break
            res.append(b_antinode)
        return res


    for freq, coords in freqs.items():
        done = set()
        for a in coords:
            for b in coords:
                if a == b or b in done:
                    continue
                new_nodes = calc_antinodes_pt2(a, b)
                for node in new_nodes:
                    i, j = node
                    mat_pt2[i][j] = '#'
            done.add(a)
    print(pretty_mat(mat_pt2))
    print(pretty_mat(mat_pt2).count('#') + len([c for c in pretty_mat(mat_pt2) if not (c == '#' or c == '.' or c == '\n')]))
