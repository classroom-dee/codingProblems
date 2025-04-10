from typing import List
def solution(n: int, s: int) -> List[int]:
    if n > s:
        return [-1]
    target = s // n
    res = []
    running = 0
    while n > 1:
        res.append(target)
        running += target
        n -= 1
        target = (s - running) // n
        
    res.append(s - sum(res))
    return res

# 11, 2
# 1, 10 -> 10    
# 2, 9 -> 18 
# 3, 8 -> 24
# 4, 7 -> 28
# 5, 6 -> 30

# 11 , 3
# 1, 1, 9
# 1, 2, 8
# 1, 3, 7
# 1, 4, 6
# 1, 5, 5
# 2, 2, 7
# 2, 3, 6
# 2, 4, 5
# 3, 3, 5
# 3, 4, 4


# 7
# 1, 1, 5
# 1, 2, 4
# 1, 3, 3
# 2, 2, 3

#