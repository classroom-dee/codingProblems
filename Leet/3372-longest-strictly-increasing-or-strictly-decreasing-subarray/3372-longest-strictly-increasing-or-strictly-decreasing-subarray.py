class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr_streak = 0
        decr_streak = 0
        max_streak = 0
        
        for i in range(len(nums)):
            if i - 1 >= 0:
                if nums[i] > nums[i - 1]:
                    incr_streak += 1
                    decr_streak = 1
                elif nums[i] < nums[i - 1]:
                    decr_streak += 1
                    incr_streak = 1
                else:
                    decr_streak = 1
                    incr_streak = 1
            else:
                incr_streak += 1
                decr_streak += 1
            max_streak = max(max_streak, max(incr_streak, decr_streak))

        return max_streak

        # cand = []
        # for k in range(1, len(nums)+1):
        #     k_len = []
        #     for i in range(len(nums)-k+1):
        #         incr = []
        #         decr = []
        #         for j in range(i, i+k):
        #             if k == 1:
        #                 incr.append(nums[j])
        #                 continue
        #             if j - 1 >= 0:
        #                 if nums[j] > nums[j-1]:
        #                     incr.append(nums[j])
        #                     decr = [nums[j]]
        #                 elif nums[j] < nums[j-1]:
        #                     decr.append(nums[j])
        #                     incr = [nums[j]]
        #                 else: # same
        #                     decr = [nums[j]]
        #                     incr = [nums[j]]
        #             else:
        #                 incr.append(nums[j])
        #                 decr.append(nums[j])
        #         if incr and len(incr) == k: k_len.append(incr) 
        #         if decr and len(decr) == k: k_len.append(decr)
        #     if k_len:
        #         cand.append(k_len)

        # return len(cand[-1][0])