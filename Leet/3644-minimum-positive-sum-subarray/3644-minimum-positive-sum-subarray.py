class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        for start in range(len(nums)):
            curr_sum = 0

            for end in range(start, min(len(nums), start + r)):
                curr_sum += nums[end]
                length = end - start + 1

                if l <= length <= r and curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)

        return min_sum if min_sum != float('inf') else -1
        
        # min_sum = -1
        # for length in range(l, r + 1):
        #     for start in range(len(nums) - length + 1):
        #         end = start + length
        #         curr_sum = sum(nums[start:end])
                
        #         if curr_sum > 0:
        #             if min_sum == -1:
        #                 min_sum = curr_sum
        #             else:
        #                 min_sum = min(min_sum, curr_sum)
                
        # return min_sum