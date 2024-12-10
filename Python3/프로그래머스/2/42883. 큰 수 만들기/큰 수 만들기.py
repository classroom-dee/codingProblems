# biggest num sol 3
def solution(number, k):
    stk = []
    for d in number:
        while k > 0 and stk and stk[-1] < d:
            stk.pop()
            k -= 1
        stk.append(d)
    if k > 0:
        stk = stk[:-k]
    return ''.join(stk)