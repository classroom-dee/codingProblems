def solution(dirs):
    # v = set()
    v = []
    mov = {"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}
    curr = (0, 0)
    for dir in dirs:
        tmp = calc(curr, mov[dir])
        if tmp != False:
            # v.add((curr, tmp))
            if {curr, tmp} not in v:
                v.append({curr, tmp})
            curr = tmp
    # print(curr)
    return len(v)

def calc(p1, p2):
    res = ((p1[0] + p2[0]), (p1[1] + p2[1]))
    if abs(res[0]) > 5 or abs(res[1]) > 5: return False
    else: return res