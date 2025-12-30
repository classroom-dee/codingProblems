class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # vals = []
        # for i, n in enumerate(nums):
        #     if n != val:
        #         vals.append(i)

        # last = 0
        # for i in range(len(vals)):
        #     nums[i] = nums[vals[i]]
        #     last = i
        
        # del nums[last+1:]
        # return len(vals)
        # --------------------------------------------
        # k = 0
        # for n in nums:
        #     if n != val:
        #         nums[k] = n
        #         k += 1
        # return k
        # --------------------------------------------
        nums[:] = [n for n in nums if n != val]
        return len(nums)