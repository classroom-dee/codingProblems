# the correct parentheses problem
def solution(s):
    from collections import deque
    dic = {'(':1, ')':-1}
    dq = deque(s)
    i, res, cnt = 0, False, 0
    while dq:
        # pop
        n = dic[dq.popleft()]
        # if i indicates the start(i == 0):
        if i == 0:
            # if the starter is -1: return
            if n == -1: return False
            # else if it's 1 : 
            else:
                # TODO:do the operation
                cnt += n
                i += 1
        # if i is not a starter (i != 0):
        else:
            # TODO: do the operation
            # progress the queue: 
            cnt += n
            # if closed properly,
            if cnt == 0:
                # conclude, start from 0 (i = 0)
                i = 0
            # if not,
            else:
                # i + 1
                i += 1
        # print(f'i:{i}, n:{n}, cnt:{cnt}, dq:{dq}')
        res = (cnt == 0)
    return res