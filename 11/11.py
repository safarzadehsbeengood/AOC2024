import sys
from functools import cache

with open(sys.argv[1], "r") as f:
    nums = list(map(int, f.read().split()))
    print(nums)

    pt1 = nums.copy()
    pt2 = nums.copy()

    # pt 1
    for _ in range(25):
        res = []
        for stone in pt1:
            if stone == 0:
                res.append(1)
                continue
            s = str(stone)
            l = len(s)
            if l % 2 == 0:
                left, right = int(s[:l//2]), int(s[l//2:])
                res.append(left)
                res.append(right)
            else:
                res.append(stone*2024)
        pt1 = res
    print(len(pt1))

    # pt 2
    @cache
    def x(num, steps):
        if steps == 0:
            return 1
        if num == 0:
            return x(1, steps-1)
        if len(str(num)) % 2 == 0:
            return x(int(str(num)[:len(str(num))//2]), steps-1) + x(int(str(num)[len(str(num))//2:]), steps-1)
        else:
            return x(num*2024, steps-1)

    print(sum(x(num, 75) for num in pt2))
