class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # # O(nlogn) solution
        # nums.sort()
        # ti = []
        
        # if nums[-1] < target or nums[0] > target:
        #     return ti
        
        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         break
        #     if nums[i] == target:
        #         ti.append(i)
        
        # return ti

        # O(n) solution
        smaller = sum(n < target for n in nums)
        equal = nums.count(target)

        return list(range(smaller, smaller + equal))