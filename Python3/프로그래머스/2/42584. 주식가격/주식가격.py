# stock value prob
def solution(prices):
    from collections import deque
    dq = deque(prices)
    res = []
    while dq:
        target = dq.popleft()
        time = 0
        for e in dq:
            time += 1
            if e < target:
                break
        res.append(time)
    return res