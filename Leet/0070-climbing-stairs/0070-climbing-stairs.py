class Solution:
    # def climbStairs(self, n: int) -> int:
        # total = 0

        # for b in range(n // 2 + 1): # number of 2-steps
        #     a = n - 2 * b           # number of 1-steps
        #     slots = a + b           # total moves

        #     # count ways to place b two-steps among all moves
        #     ways_for_this_pair = 1
        #     for i in range(1, b + 1):
        #         ways_for_this_pair = ways_for_this_pair * (slots - i + 1) // i

        #     total += ways_for_this_pair

        # return total
    
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2

        if n <= 2:
            return n
        
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b
    