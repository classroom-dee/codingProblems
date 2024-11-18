def solution(n):
    res = seq_non_recurse(n)
    return res % 1234567 
def seq_non_recurse(n):
    n0, n1, n2 = 0, 1, 0
    for _ in range(2, n+1):
        n2 = n0 + n1
        n0 = n1
        n1 = n2
    return n2