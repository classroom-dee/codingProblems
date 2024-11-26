import math
def solution(n, k):
    d = []
    while n > 0:
        rem = n % k
        d.append(str(rem))
        n = n // k
    d.reverse()
    d = ''.join(d).split('0')
    cnt = 0
    for e in d:
        cnt += prime(int(e)) if e != '' else 0
    return cnt
def prime(n):
    if n <= 1: return False
    if n <= 3: return True 
    if n % 2 == 0 or n % 3 == 0:
        return False
    # if > 3 ---> 6k +- 1 = prime
    # n = c * d ---> c >= sqrt(n) or d >= sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True