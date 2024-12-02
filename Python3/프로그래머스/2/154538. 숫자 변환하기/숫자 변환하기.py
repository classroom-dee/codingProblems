def solution(x, y, n):
    from collections import deque
    dq = deque([(x, 0)])
    rec = set()
    
    while dq:
        curr, cnt = dq.popleft()
        if curr == y: return cnt
        if curr in rec: continue
        if curr > y: continue
        rec.add(curr)
        dq.append((curr * 3, cnt + 1))
        dq.append((curr * 2, cnt + 1))
        dq.append((curr + n, cnt + 1))

    return -1