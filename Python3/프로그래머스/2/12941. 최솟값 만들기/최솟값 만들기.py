# min value gen prob
def solution(a, b):
    a = sorted(a)
    b = sorted(b, reverse=True)
    tot = 0
    for e1, e2 in zip(a, b):
        tot += e1 * e2
    return tot