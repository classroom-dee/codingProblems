# no permutation no combination
def solution(sizes):
    n = len(sizes)
    # dp[i][j] will store the minimum cost of multiplying Ai...Aj
    # j mats == j*j possible mult hence,
    dp = [[0] * n for _ in range(n)]
    # optimal split
    # split = [[0] * n for _ in range(n)]
    
    # mats mult chain (2 mats, 3 mats, ... n mats)
    for length in range(2, n + 1):
        # starting mats, diminishing
        for i in range(n - length + 1):
            # end of mult chain, incremental
            # l2: 0~1 1~2 2~3 3~4, l3: 0~2 1~3 2~4... ASO, ASF
            j = i + length - 1
            dp[i][j] = float("inf") # this has smaller footprint than sys.maxsize
            # split points k
            for k in range(i, j):
                # (first mat~splitter mats mult cost)
                # + (next to splitter~last mats mult cost)
                # + (first mat row x splitter mat col x last mat col)
                cost = (
                    dp[i][k] 
                    + dp[k+1][j] 
                    + sizes[i][0] * sizes[k][1] * sizes[j][1]
                )
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    # split[i][j] = k
    return dp[0][n-1]