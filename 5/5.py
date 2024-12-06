import sys

with open(sys.argv[1], "r") as f:
    text = f.read()
    rules, updates = text.split("\n\n")
    # print(rules)
    # print(updates)

    rule = {}
    for r in rules.splitlines():
        a, b = r.split('|')
        if rule.get(a) == None:
            rule[a] = {
                "after": set(b),
                "before": set(),
            }
        else:
            rule[a]["after"].add(b)
        if rule.get(b) == None:
            rule[b] = {
                "after": set(),
                "before":set(a),
            }
        else:
            rule[b]["before"].add(a)

    def eval_update(update):
        seen = set()
        for i in range(len(update)-1):
            # print(seen)
            num = update[i]
            if rule.get(num) is None:
                seen.add(num)
                continue
            before = rule[num]["before"]
            after = rule[num]["after"]
            if any([x in after for x in seen]) or any([x in before for x in update[i+1:]]):
                # print()
                # print(f'err: {num} in {nums}')
                # print(rule[num]["before"], rule[num]["after"])
                return False
            seen.add(num)
        return True

    # pt 1
    res = 0
    for update in updates.splitlines():
        nums = update.split(',')
        if eval_update(nums):
            res += int(nums[len(nums)//2])
            
    print(res)

    print("-"*20)

    # pt 2
    res = 0

    def get_next(nums):
        if not nums:
            return -1
        n = set()
        after_sets = [rule[m]["after"] for m in nums]
        for s in after_sets:
            n = n.union(s)
        n = n.intersection(set(nums))
        n = set(nums).difference(n)
        return n.pop()
            
    for update in updates.splitlines():
        result = []
        nums = update.split(',')
        if not eval_update(nums):
            untracked_list = [num for num in nums if rule.get(num) == None] 
            new_list = [num for num in nums if rule.get(num) != None] 
            while new_list:
                next = get_next(new_list)
                new_list.pop(new_list.index(next))
                result.append(next)
            result += untracked_list
            res += int(result[len(result)//2])
    print(res)
