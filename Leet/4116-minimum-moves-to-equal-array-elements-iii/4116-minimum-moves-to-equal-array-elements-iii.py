class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        total = 0
        for n in nums:
            total += target - n

        # nums.sort()
        # target = nums[-1]
        # total = 0
        
        # for n in nums:
        #     if n == target:
        #         break
        #     total += target - n
        
        return total