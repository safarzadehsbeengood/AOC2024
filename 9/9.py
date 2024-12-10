import sys

with open(sys.argv[1], "r") as f:
    text = f.read()[:-1]
    # id: (size, space_after)
    files = {}
    id = 0
    for i in range(0, len(text)-1, 2):
        files[id] = (int(text[i]), int(text[i+1]))
        id += 1
    files[id] = (int(text[-1]), 0)
    # print(files)

    def eval(files: dict):
        # print(files)
        n = sum([x[0] for x in files.values()])
        res = 0
        pos = 0
        # start at first file id
        id = 0
        # last file id
        pull_id = len(files.keys())-1
        while True:
            if pos > n-1:
                break
            size, space_after = files[id]
            pos += size
            res += sum([id * p for p in range(pos-size, pos)])
            # for p in range(pos-size, pos):
            #     print(f'ORIG {p} * {id} = {p*id} -> {res}')
            while space_after > 0:
                if pos >= n-1:
                    break
                if files[pull_id][0] <= 0:
                    pull_id -= 1
                res += pull_id * pos
                # print(f'MOVED {pos} * {pull_id} = {pull_id*pos} -> {res}')
                space_after -= 1
                pos += 1
                files[pull_id] = (files[pull_id][0]-1, files[pull_id][1])
            id += 1
        print(res)

    files2 = {}
    id = 0
    for i in range(len(text)):
        if i == 0:
            files2[id] = {
                "size": int(text[i]),
                "start": 0
            }
            continue
        if i % 2 == 0:
            files2[id] = {
                "size": int(text[i]),
                "start": files2[id-1]["start"] + files2[id-1]["size"] + files2[id-1]["space_after"]
            }
        else:
            files2[id]["space_after"] = int(text[i])
            id += 1
    files2[len(files2.keys())-1]["space_after"] = 0

    def eval_2(files: dict):
        def find_spot(id):
            valid = [file_id for file_id, file_info in files.items() if file_info["space_after"] >= files[id]["size"] and file_info["start"] < files[id]["start"]]
            if valid:
                valid.sort(key=lambda x: files[x]["start"], reverse=True)
                chosen = valid.pop()
                # print(files[chosen]["start"])
                # print(f"MOVE {id} in front of {chosen}")
                # set moved file's new start location
                files[id]["start"] = files[chosen]["start"] + files[chosen]["size"]
                # set moved file's new free space after
                files[id]["space_after"] = files[chosen]["space_after"]-files[id]["size"]
                # set chosen file's new space after to 0, since the moved file is right in front
                files[chosen]["space_after"] = 0
        for id in list(files.keys())[::-1]:
            find_spot(id)
        res = 0
        for file_id, file_info in files.items():
            start, size = file_info["start"], file_info["size"]
            res += sum([file_id*p for p in range(start, start+size)])
        print(res)

    eval(files)
    # print(files2)
    eval_2(files2)
