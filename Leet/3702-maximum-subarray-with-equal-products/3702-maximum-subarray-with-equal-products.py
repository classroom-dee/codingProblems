from math import gcd, lcm, prod
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        for length in range(len(nums), 0, -1):
            for start in range(len(nums) - length + 1):
                # end = start + length - 1
                snub_arr = nums[start:start + length]
                if prod(snub_arr) == gcd(*snub_arr) * lcm(*snub_arr):
                    return len(snub_arr)
                
