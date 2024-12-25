# from collections import Counter
# from itertools import permutations
# def solution(orders, course):
#     cnt = Counter()
#     course_cnt = {c:0 for c in course}
#     for o in orders:
#         for c in course:
#             tmp = set()
#             if c <= len(o):
#                 perm = permutations(o, c)
#                 for p in perm:
#                     cnt[p] += 1
#                     # cnt[tuple(sorted(p))] += 1
#                     course_cnt[c] = max(course_cnt[c], cnt[p])
#     res = set()
#     print(course_cnt)
#     for c in course_cnt:
#         if course_cnt[c] > 1:
#             for perm in cnt:
#                 if cnt[perm] == course_cnt[c] and len(perm) == c:
#                     res.add(tuple(sorted(perm)))
#     return sorted(''.join(e) for e in res)
# The optimized version of the above
from collections import Counter
from itertools import combinations
def solution(orders, course):
    res = []
    for c in course:
        cnt = Counter()
        for o in orders:
            if len(o) >= c:
                comb = combinations(sorted(o), c)
                cnt.update(comb)
        max_count = max(cnt.values(), default=0)
        if max_count > 1:
            res += [''.join(k) for k, v in cnt.items() if v == max_count]
    return sorted(res)