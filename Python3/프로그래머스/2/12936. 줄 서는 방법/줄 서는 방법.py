# from itertools import permutations
# def solution(n, k):
#     ppl = [i+1 for i in range(n)]
#     res = permutations(ppl, len(ppl))
#     return list(res)[k-1]
import math
def solution(n, k):
    ppl = [i + 1 for i in range(n)]
    k -= 1
    res = []

    for i in range(n, 0, -1):
        f = math.factorial(i - 1)
        idx = k // f
        res.append(ppl.pop(idx))
        k %= f
    return res