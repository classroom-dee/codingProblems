class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        mx = nums[0]

        mn_suff = [0] * len(nums)
        mn_suff[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            mn_suff[i] = min(nums[i], mn_suff[i + 1])

        for i in range(len(nums)):
            if i == 0:
                if mx - mn_suff[i] <= k:
                    return i
            else:
                mx = max(mx, nums[i])
                # mn = min(nums[i:])
                mn = mn_suff[i]
                if mx - mn <= k:
                    return i

        return -1
            
            