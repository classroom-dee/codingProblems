def solution(info, n, m):
    from collections import deque

    # Initialize DP table: dp[a][b] = True if A has 'a' traces and B has 'b' traces
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True  # Start with no traces

    for item in info:
        a_trace, b_trace = item
        # Prepare next DP state
        next_dp = [[False] * m for _ in range(n)]

        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue
                # Option 1: assign this item to A (if it won't exceed limit)
                if a + a_trace < n:
                    next_dp[a + a_trace][b] = True
                # Option 2: assign to B (if it won't exceed limit)
                if b + b_trace < m:
                    next_dp[a][b + b_trace] = True

        dp = next_dp  # Update DP

    # Find the minimal A trace count that is valid
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a

    return -1  # No valid assignment found
