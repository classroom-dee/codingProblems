from collections import deque
def solution(n):
    res = search(n)
    return res
def search(n):
    dq = deque(sorted(range(1, n+1), reverse=True))
    cnt = 0
    while dq:
        tot = 0
        target = dq.popleft()
        for i in range(target, 0, -1):
            tot += i
            if tot == n:
                cnt += 1
                break
            elif tot > n:
                break
            else:
                continue
    return cnt