import sys
from tqdm import tqdm

A = "A"
B = "B"
T = "T"

with open(sys.argv[1], "r") as f:
    text = [prize.splitlines() for prize in f.read().split('\n\n')]
    prizes = []
    for prize in text:
        d = {}
        a = int(prize[0].split(':')[1].split('+')[1].split(',')[0]), int(prize[0].split(':')[1].split('+')[2])
        b = int(prize[1].split(':')[1].split('+')[1].split(',')[0]), int(prize[1].split(':')[1].split('+')[2])
        target = tuple(map(int, prize[2].split('Prize: X=')[1].split(', Y=')))
        d[A] = a
        d[B] = b
        d[T] = target
        prizes.append(d)

    def x(a, b, target):
        ax, ay = a
        bx, by = b
        tx, ty = target
        min_tokens = float("inf")
        winnable = False
        for i in range(1000):
            for j in range(1000):
                if ax*i + bx*j == tx and ay*i + by*j == ty:
                    winnable = True
                    if i*3+j < min_tokens:
                        min_tokens = i*3+j
        return min_tokens if winnable else 0


    # pt 1 (inefficient)
    res = 0
    with tqdm(total=len(prizes)) as pbar:
        for prize in prizes:
            a = prize[A]
            b = prize[B]
            t = prize[T]
            res += x(a, b, t)
            pbar.update()
        print(res)


    # pt 2 (efficient)
    for prize in prizes:
        ax, ay = prize[A]
        bx, by = prize[B]
        tx, ty = prize[T]
        tx += 10000000000000
        ty += 10000000000000
        ca = (tx*by-ty*bx) / (ax*by-ay*bx)
        cb = (tx-ax*ca) / bx
        res += ca*3+cb if ca % 1 == 0 and cb % 1 == 0 else 0

    print(int(res))
