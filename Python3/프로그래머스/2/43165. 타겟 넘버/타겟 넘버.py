def solution(nambaz, target):
    from collections import deque
    rec = set()
    stk = deque([(0, 0, tuple())]) # sum, idx, record
    l = len(nambaz)
    while stk:
        curr = stk.pop()
        # print(curr)
        if curr[1] == l:
            if curr[0] > target: continue
            if curr[0] == target:
                if curr[2] not in rec:
                    rec.add(curr[2])
            continue
        stk.append((curr[0] + nambaz[curr[1]], curr[1] + 1, curr[2] + (nambaz[curr[1]],)))
        stk.append((curr[0] + (nambaz[curr[1]] * -1), curr[1] + 1, curr[2] + ((nambaz[curr[1]] * -1),)))
    return len(rec)