class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # 2nd attemp with DP...
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                # Get possible XOR values from above
                # Get possible XOR values from the left
                # XOR each with grid[i][j]
                # Add the results to dp[i][j]
                if i > 0:
                    for x in dp[i-1][j]:
                        dp[i][j].add(x ^ grid[i][j])
                if j > 0:
                    for x in dp[i][j-1]:
                        dp[i][j].add(x ^ grid[i][j])
        
        return min(dp[-1][-1])

        # stack = [(0, 0, grid[0][0])]
        # min_xor = None
        # visited = set()

        # def _is_out_of_boundary(i, j):
        #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        #         return True
        #     return False

        # while stack:
        #     m, n, cost = stack.pop()
        #     if (m, n, cost) in visited:
        #         continue
        #     visited.add((m, n, cost))
            
        #     if m == len(grid) - 1 and n == len(grid[0]) - 1:
        #         if min_xor is None:
        #             min_xor = cost
        #         else:
        #             min_xor = min(min_xor, cost)
                
        #         continue

        #     right = (m, n + 1)
        #     if not _is_out_of_boundary(right[0], right[1]): 
        #         right_cost = cost ^ grid[right[0]][right[1]]
        #         stack.append((*right, right_cost))
            
        #     down = (m + 1, n)
        #     if not _is_out_of_boundary(down[0], down[1]):
        #         down_cost = cost ^ grid[down[0]][down[1]]
        #         stack.append((*down, down_cost))
        
        # return min_xor