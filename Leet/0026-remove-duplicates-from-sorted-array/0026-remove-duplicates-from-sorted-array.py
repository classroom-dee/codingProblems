class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        w = 1
        for r in range(1, len(nums)):
            # bc nums is sorted
            if nums[r] != nums[w - 1]:
                nums[w] = nums[r]
                w += 1
        del nums[w:]          # truncate in place
        return w