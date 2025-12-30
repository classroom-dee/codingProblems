class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rec = set()
        i = 0
        nums_len = len(nums)

        while i < nums_len:
            curr = nums[i]
            if nums[i] in rec:
                nums.pop(i)
            else:
                i += 1
            rec.add(curr)
            nums_len = len(nums)
        return len(nums)