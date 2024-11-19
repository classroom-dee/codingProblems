# mister/missus technicality long jump athlete prob
def solution(n):
    s1, s2 = 1, 2
    res = jump(n, s1, s2)
    return res % 1234567

def jump(n, s1, s2):
    # edge cases
    if n == 1:
        return s1
    if n == 2:
        return s2
    # init
    grids = [0] * (n + 1)
    grids[1] = s1
    grids[2] = s2
    # Godbonacci seq
    for i in range(3, n + 1):
        grids[i] = grids[i - 1] + grids[i - 2]
    return grids[n]