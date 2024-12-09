import math
from itertools import permutations
def solution(numbers):
    s = set()
    for i in range(len(numbers)):
        num_perm = permutations(numbers, i+1)
        for p in num_perm:
            targ = int(''.join(p))
            if prime(targ): s.add(targ)
    return len(s)
def prime(n):
    # d = []
    # for i in range(1, n+1):
    #     d.append(n % i == 0)
    # return sum(d) == 2
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True