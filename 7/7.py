from itertools import product
import sys
from tqdm import tqdm
with open(sys.argv[1], "r") as f:
    lines = f.read().split('\n')[:-1]
    op_perm_map = {}

    def eval_op_perm(operands: list[int], perm: str, target: int):
        if len(perm) != len(operands)-1:
            return False
        res = operands[0]
        i = 0
        while i < len(perm):
            op = perm[i]
            x = operands[i+1]
            if op == '+':
                res += x
            elif op == '*':
                res *= x
            elif op == '|':
                res = int(str(res) + str(x))
            i += 1
            # print(f'{target}: {operands} -> {perm} -> {res}')
        return res == target

    pt1 = 0
    with tqdm(total=len(lines)) as pbar:
        for line in lines:
            n, operands = int(line.split(':')[0]), list(map(int, line.split(':')[1].strip().split()))
            perms = None
            valid = False

            if len(operands)-1 in op_perm_map.keys():
                perms = op_perm_map[len(operands)-1]
            else:
                perms = [''.join(p) for p in list(product(['*', '+', '|'], repeat=len(operands)-1))]
                op_perm_map[len(operands)-1] = list(perms)

            for perm in perms:
                if eval_op_perm(operands, perm, n):
                    valid = True
                    break
            if valid:
                pt1 += n
            pbar.update()
    print(pt1)

