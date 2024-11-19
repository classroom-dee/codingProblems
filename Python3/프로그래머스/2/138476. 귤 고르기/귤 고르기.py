# greedy mandarin pickin' prob
def solution(k, mand):
    from collections import Counter, deque
    cnt = Counter(mand)
    srt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
    dq = deque(srt)
    res = set()
    total = 0
    while True:
        if total == k:
            return len(res)
        pick = dq.popleft()
        space = k - total
        if space >= pick[1]:
            total += pick[1]
        else:
            total += space
        res.add(pick[0])