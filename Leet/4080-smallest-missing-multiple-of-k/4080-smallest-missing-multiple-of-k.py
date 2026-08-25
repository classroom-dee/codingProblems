class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        # if nums were [5, 10, 15], the missing one would be 20, so +k+1 is needed
        for n in range(k, max(nums) + k + 1, k): 
            # print(n)
            if n not in num_set:
                return n
        return -1