import sys
import re
from PIL import Image
import numpy as np


with open(sys.argv[1]) as f:
    text = f.read()
    m, n = 103, 101
    print(f'{m}x{n} = {m*n}')

    def griddy(robots):
        padding = 0
        coordinates = list(robots.keys())
        min_x = min(x for x, _ in coordinates)
        max_x = max(x for x, _ in coordinates)
        min_y = min(y for _, y in coordinates)
        max_y = max(y for _, y in coordinates)
    
    # Calculate dimensions with padding
        width = max_x - min_x + 1 + (2 * padding)
        height = max_y - min_y + 1 + (2 * padding)

        arr = np.zeros((height, width), dtype=np.uint8)
        for (y, x), ct in robots.items():
            if ct > 0:
                adjx = x-min_x+padding
                adjy = y-min_y+padding
                arr[adjx, adjy] = 255
        return Image.fromarray(arr)


    def eval(secs):
        robots = {}

        for i in range(m):
            for j in range(n):
                robots[(i, j)] = 0
        for robot in text.splitlines():
            x = re.findall(r'-?\d+,-?\d+', robot)
            p, v = tuple(map(int, x[0].split(','))), tuple(map(int, x[1].split(',')))
            vx, vy = v
            px, py = p

            py = (py + (secs * vy)) % m
            px = (px + (secs * vx)) % n

            robots[(py, px)] += 1

        bx, by = (n-1)//2, (m-1)//2
        q1, q2, q3, q4 = 0, 0, 0, 0
        for (y, x), ct in robots.items():

            if ct == 0:
                continue
            # q1
            if x < bx and y < by:
                q1 += ct
            # q2
            elif x < bx and y > by:
                q2 += ct
            # q3
            elif x > bx and y > by:
                q3 += ct
            # q4
            elif x > bx and y < by:
                q4 += ct
        img = griddy(robots)
        # return (img[0], img[1], q1*q2*q3*q4) if img[0] < 3000 else None
        img.save(f"./pics/{secs}_{q1*q2*q3*q4}.png")


    # with tqdm(total=n) as pbar:
    for i in range(7000):
        print(i)
        eval(i)
            # pbar.update()

