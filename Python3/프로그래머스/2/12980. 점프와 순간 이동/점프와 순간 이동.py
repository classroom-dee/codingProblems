def solution(n):
    # jump dist of k -> dist: k, energy: k
    # tp -> dist: (curr-start)x2, energy: 0
    # minimize the num of jumps given the target n
    pow = 0
    while n >= 1:
        if n % 2 != 0:
            pow += 1
            n -= 1
        else:
            n //= 2
    return pow