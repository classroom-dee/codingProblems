def solution(order):
    from collections import deque
    correct = [order[o-1] for o in order]
    dq = deque(order)
    temp = []
    idx = 0
    while dq or temp:
        if dq and correct[idx] == dq[0]:
            dq.popleft()
            idx += 1
        elif temp and correct[idx] == temp[-1]:
            temp.pop()
            idx += 1
        elif dq:
            temp.append(dq.popleft())
        else:
            break
    return idx