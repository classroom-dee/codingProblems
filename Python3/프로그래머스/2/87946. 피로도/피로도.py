# fatigue prob
from itertools import permutations
def solution(k, dungeons):
    n = range(len(dungeons))
    perm = permutations(n)
    done = set()
    for p in perm:
        curr = k
        trav = tuple()
        for i in p:
            if dungeons[i][0] <= curr:
                curr -= dungeons[i][1]
                trav += (i,)
            else:
                break
        done.add(trav)
    res = max(done, key=lambda x: len(x))
    return len(res)