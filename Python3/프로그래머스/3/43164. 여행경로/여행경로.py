def solution(tickets):
    # init itinerary
    dic = {}
    for t in tickets:
        dic[t[0]] = dic.get(t[0], []) + [t[1]]
    for it in dic:
        dic[it].sort(reverse=True)
    
    # traverse
    stk = ["ICN"]
    res = []
    while stk:
        target = stk[-1]
        if target not in dic or not dic[target]: # used up
            res.append(stk.pop())
        else:
            stk.append(dic[target][-1])
            dic[target] = dic[target][:-1]
    return res[::-1]