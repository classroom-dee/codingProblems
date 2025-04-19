
def solution(m, n, puddles):
    # if the map is flat
    if m == 1 or n == 1:
        return 0 if puddles and puddles[0] else 1
    
    # n -> row m -> col
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    # convert to row, col and 0-index it, and then to set
    puddles = set((e[1] - 1, e[0] - 1) for e in puddles)
    
    # start cant be a puddle
    dp[0][0] = 1
    
    #1     (2, 2), (1, 3)
    #2 (2, 1), (1, 2), (0, 3)
    # sum of top and left is self
    for r in range(n):
        for c in range(m):
            if (r, c) not in puddles:
                # top-left inherits directly
                if r > 0:
                    dp[r][c] += dp[r - 1][c]
                if c > 0:
                    dp[r][c] += dp[r][c - 1]
            else:
                dp[r][c] = 0
    return dp[n - 1][m - 1] % 1000000007