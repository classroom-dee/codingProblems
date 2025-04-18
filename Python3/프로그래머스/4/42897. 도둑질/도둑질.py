def solution(money):
    
    # only one can be chosen among 3
    if len(money) == 3:
        return max(money)
    
    # last exclusion
    prev = curr = 0
    for num in money[:-1]:
        added = prev + num
        prev, curr = curr, max(curr, added)
    
    res1 = curr
    
    # first exclusion
    prev = curr = 0
    for num in money[1:]:
        added = prev + num
        prev, curr = curr, max(curr, added)
    
    res2 = curr
    
    return max(res2, res1)