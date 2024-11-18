def solution(n):
    a = cnt(n)
    # print(bin(n), end=' ')
    while True:
        n += 1
        if a == cnt(n):
            # print(bin(n))
            break
    return n
def cnt(n):
    one = 0
    while n > 0:
        if n & 1:
            one += 1
        n >>= 1
    return one