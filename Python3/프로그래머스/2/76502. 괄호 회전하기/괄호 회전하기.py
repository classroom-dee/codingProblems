# parentheses closure prob 2
def solution(s):
    from collections import deque
    correct, l = {'{}', '[]', '()'}, len(s)
    res = 0
    dq = deque(s)
    for _ in range(l-1):
        res += check(dq, correct)
        f = dq.popleft()
        dq.append(f)
    return res

def check(dq, correct):
    stk = []
    for e in dq:
        stk.append(e)
        if len(stk) >= 2:
            if ''.join(stk[-2:]) in correct:
                stk.pop()
                stk.pop()
    return 1 if len(stk) == 0 else 0