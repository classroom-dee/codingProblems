# cache prob
from collections import deque
def solution(size, cities):
    used = deque()
    cities = deque(cities)
    HIT, MISS, time = 1, 5, 0
    if size == 0 : return len(cities) * MISS
    while cities:
        c = cities.popleft().lower()
        if c in used:
            used.remove(c)
            used.append(c)
            time += HIT
        else:
            if len(used) >= size:
                used.popleft()
            used.append(c)
            time += MISS
    return time