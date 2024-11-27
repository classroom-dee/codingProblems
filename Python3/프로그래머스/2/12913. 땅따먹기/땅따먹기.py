# hopscotch prob
def solution(land):
    rows = len(land)
    cols = 4

    # init 1st row
    cnt = [[0] * cols for _ in range(rows)]
    for j in range(cols):
        cnt[0][j] = land[0][j]
    
    # sum up
    for i in range(1, rows):
        for j in range(cols):
            # add to previous max sums
            m = max(cnt[i-1][x] for x in range(cols) if x != j)
            # assign to current row counter
            cnt[i][j] = land[i][j] + m
            
    # hence the maximum last row
    return max(cnt[-1])