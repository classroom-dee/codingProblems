class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import lcm
        from itertools import combinations

        def _do_it(x):
            total = 0
            for i in range(1, len(coins) + 1):
                for c in combinations(coins, i):
                    if i % 2 != 0:
                        total += x // lcm(*c)
                    else:
                        total -= x // lcm(*c)
            return total

        left, right = 1, min(coins) * k
        while left <= right:
            x = left + (right - left) // 2
            res = _do_it(x)
            if res < k:
                left = x + 1
            else:
                right = x - 1
        
        return left

