class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cand = []
        for k in range(1, len(nums)+1):
            k_len = []
            for i in range(len(nums)-k+1):
                incr = []
                decr = []
                for j in range(i, i+k):
                    if k == 1:
                        incr.append(nums[j])
                        continue
                    if j - 1 >= 0:
                        if nums[j] > nums[j-1]:
                            incr.append(nums[j])
                            decr = [nums[j]]
                        elif nums[j] < nums[j-1]:
                            decr.append(nums[j])
                            incr = [nums[j]]
                        else: # same
                            decr = [nums[j]]
                            incr = [nums[j]]
                    else:
                        incr.append(nums[j])
                        decr.append(nums[j])
                if incr and len(incr) == k: k_len.append(incr) 
                if decr and len(decr) == k: k_len.append(decr)
            if k_len:
                cand.append(k_len)

        return len(cand[-1][0])

                    