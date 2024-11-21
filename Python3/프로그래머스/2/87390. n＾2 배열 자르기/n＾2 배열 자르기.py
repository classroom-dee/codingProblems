# array slicing
def solution(n, left, right):
    # arr = [[0]*n for _ in range(n)]
    # # one_dim = []
    # for i in range(1, n+1):
    #     for k in range(i):
    #         arr[i-1][k] = i
    #         arr[k][i-1] = i
    # for e in arr:
    #     one_dim += e
    # res = one_dim[left:right+1]
    res = []
    for i in range(left, right+1):
        r, c = i // n, i % n 
        # print(f'idx {i}, row:{r}, col:{c}')
        v = max(r, c) + 1
        res.append(v)
    return res