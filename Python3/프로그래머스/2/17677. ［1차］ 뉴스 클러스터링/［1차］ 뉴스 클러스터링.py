# similarity
from collections import Counter
def solution(str1, str2):
    unicode = range(ord('a'), ord('z') + 1)
    mset1, mset2 = perm(str1, unicode), perm(str2, unicode)
    set1, set2 = set(mset1), set(mset2)
    inter = set1.intersection(set2)
    union = set1.union(set2)
    i_cnt, u_cnt = 0, 0
    for i in inter:
        i_cnt += min(mset1[i], mset2[i])
    for u in union:
        u_cnt += max(mset1[u], mset2[u])
    if u_cnt == 0: return 65536
    return int(i_cnt / u_cnt * 65536)
def perm(s, unicode):
    s = s.lower()
    res = Counter()
    for i in range(1, len(s)):
        if ord(s[i]) not in unicode or ord(s[i-1]) not in unicode: continue
        targ = s[i-1:i+1]
        res[targ] += 1
    return res