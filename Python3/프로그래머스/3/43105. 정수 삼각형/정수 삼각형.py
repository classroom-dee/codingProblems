def solution(triangle):
    # make a dp table
    dp = [[0 for _ in r] for r in triangle] # complexity 125250

    for i, row in enumerate(triangle):
        for j, num in enumerate(row):
            if i == 0:
                dp[i][j] = num
            else:
                # j is the last index
                if j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                # j is in the middle and between the crosshair
                else:
                    dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])

    return max(dp[-1])