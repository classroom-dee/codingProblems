# sweetroll prob
def solution(topping):
    ## Sol 1
    # from collections import deque
    # t_dq = deque(topping)
    # l = len(topping) - 1
    # cnt = 0
    # other_slc = []
    # for _ in range(l):
    #     other_slc.append(t_dq.popleft())
    #     cnt += (len(set(other_slc)) == len(set(t_dq)))
    # return cnt
    ## Sol 2
    from collections import Counter
    # Universal counters for each
    cheol, son_frere = Counter(), Counter(topping)
    # Uniq counters for each
    cheol_unq, frere_unq = 0, len(son_frere)

    l = len(topping)
    res = 0

    # move to the right
    for i in range(l):
        # handle Cheol's share
        cheol[topping[i]] += 1
        if cheol[topping[i]] == 1: cheol_unq += 1
        # handle brother's share
        son_frere[topping[i]] -= 1
        if son_frere[topping[i]] == 0: frere_unq -= 1
        # comparison
        res += (cheol_unq == frere_unq)
    return res