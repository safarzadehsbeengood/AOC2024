with open("input.txt", "r") as f:
    lines = f.readlines()
    levels = []
    for line in lines:
        levels.append([int(num) for num in line.split()])

    # pt 1
    def check(arr):
        return all(abs(num) > 0 and abs(num) <= 3 for num in arr) and (all(num > 0 for num in arr) or all(num < 0 for num in arr))

    safe = 0
    for level in levels:
        diffs = [level[i+1]-level[i] for i in range(len(level)-1)]
        if check(diffs):
            safe += 1
    print(safe)

    # pt 2
    def check2(level):
        diffs = [level[i+1]-level[i] for i in range(len(level)-1)]
        if set(diffs) <= { 1, 2, 3 } or set(diffs) <= { -1, -2, -3 }:
            return True
        return False
    safe = 0
    for level in levels:
        for i in range(len(level)):
            if any([check2(level[:i] + level[i+1:]) for i in range(len(level))]):
                safe += 1
                break
    print(safe)


        
