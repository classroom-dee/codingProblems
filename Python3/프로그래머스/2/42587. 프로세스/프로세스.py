def solution(pri, loc):
    from collections import deque
    proc = deque([(i, p) for i, p in enumerate(pri)])
    cnt = 0
    while proc:
        target = proc.popleft()
        if sum(map(lambda x: x[1] > target[1], proc)):
            proc.append(target)
        else:
            cnt += 1
            if target[0] == loc:
                return cnt 
    return cnt