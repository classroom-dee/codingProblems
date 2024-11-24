def solution(msg):
    d = {chr(i + 64): i for i in range(1, 27)}
    n = 26
    l = len(msg)
    res = []

    idx = 0
    while idx < l:
        j = 1
        while idx + j <= l and msg[idx:idx + j] in d:
            j += 1
        res.append(d[msg[idx:idx + j - 1]]) # current valid
        # print(res)
        if idx + j - 1 < l: # next
            n += 1
            d[msg[idx:idx + j]] = n
        # if len(res) == 10: break
        idx += j - 1 # last of the next 
    return res