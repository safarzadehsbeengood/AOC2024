with open("input.txt", "r") as f:
    # pt. 1
    lines = f.readlines()
    sum = 0
    a, b = sorted([int(line.split()[0]) for line in lines]), sorted([int(line.split()[1]) for line in lines])
    n = len(a)
    for left, right in zip(a, b):
        sum += abs(left - right)
    print(sum)

    # pt 2
    cts = {}
    for num in a:
        if cts.get(num):
            continue
        else:
            cts[num] = b.count(num)
    score = 0
    for num, count in cts.items():
        score += num * count
    print(score)