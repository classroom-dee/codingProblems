def solution(numbers):
    l = len(numbers)
    res = [-1] * l
    stk = []
    for i in range(l - 1, -1, -1):
        while stk and stk[-1] <= numbers[i]:
            stk.pop()
        if stk:
            res[i] = stk[-1]
        stk.append(numbers[i])
    return res
    # from collections import deque
    # numbers.reverse()
    # stk, res = deque(), []
    # l = len(stk)
    # for n in numbers:
    #     if l == 0:
    #         l += 1
    #         res.append(-1)
    #         stk.append(n)
    #     else:
    #         l += 1
    #         init = stk.copy()
    #         while stk:
    #             targ = stk.pop()
    #             if targ > n:
    #                 res.append(targ)
    #                 stk.append(targ)
    #                 stk.append(n)
    #                 break
    #             else:
    #                 stk.appendleft(targ)
    #                 if stk == init: 
    #                     res.append(-1)
    #                     stk.append(n)
    #                     break
    # res.reverse()
    # return res