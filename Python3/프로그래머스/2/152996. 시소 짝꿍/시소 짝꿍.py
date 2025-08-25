from collections import Counter

def solution(weights):
    dists = (2, 3, 4)
    c = Counter(weights)
    res = 0

    # people with ident weights
    for w, n in c.items():
        if n > 1:
            res += n * (n - 1) // 2

    # ...with diff weights
    for w, n in c.items():
        for d1 in dists:
            for d2 in dists:
                if d1 == d2:
                    continue
                num = w * d1
                if num % d2 == 0:
                    t = num // d2
                    if t in c and t > w:
                        res += n * c[t]
    return res