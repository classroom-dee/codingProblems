from collections import deque
from math import ceil
def solution(progresses, speeds):
    work = deque(zip(progresses, speeds))
    passed = 0
    releases = []
    while work:
        item = work.popleft()
        days = ceil((100 - item[0]) / item[1])
        # print(f'it will take {days} days to finish for work {item}')
        if days <= passed:
            releases[-1] += 1
        else:
            releases.append(1)
            passed = days
    return releases