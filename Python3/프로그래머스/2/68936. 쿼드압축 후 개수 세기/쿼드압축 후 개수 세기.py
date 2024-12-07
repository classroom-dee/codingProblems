# quad tree sol 2
def solution(arr):
    def recurse(x, y, n):
        init = arr[x][y]
        same = True
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    same = False
                    break
            if not same: break
        
        if same:
            res[init] += 1
        else:
            half = n // 2
            recurse(x, y, half) # quad 1
            recurse(x, y + half, half) # quad 2
            recurse(x + half, y, half) # quad 3
            recurse(x + half, y + half, half) # quad 4
    
    n = len(arr)
    res = [0, 0]
    recurse(0, 0, n)
    return res