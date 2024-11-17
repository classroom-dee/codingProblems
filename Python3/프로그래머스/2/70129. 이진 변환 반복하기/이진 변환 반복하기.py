# custom binary transform problem
def solution(s):
    l = len(s)
    cnt = 0
    zeros = 0
    while l > 1:
        s, rmvd = bainari(s)
        l = len(s)
        cnt += 1
        zeros += rmvd
    return [cnt, zeros]
def bainari(s):
    cnt = s.count('0')
    s = s.replace('0', '')
    s = bin(len(s))[2:]
    return [s, cnt]