import re
def eval_mul(exp):
    a, b = tuple(map(int, exp[exp.find('(')+1:exp.find(')')].split(",")))
    return a * b

with open("input.txt", "r") as f:
    text = f.read()

    # pt 1
    mul_pat = r'mul\(\d+,\d+\)'
    mul_matches = re.findall(mul_pat, text)

    res = 0
    for match in mul_matches:
        res += eval_mul(match)

    print(res)

    # pt 2
    full_pat = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    pt_2_txt = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    matches = re.findall(full_pat, text)
    enabled = True
    res = 0
    for match in matches:
        if match == "do()":
            enabled = True
            continue
        if match == "don't()":
            enabled = False
            continue
        if enabled:
            res += eval_mul(match)
    print(res)
