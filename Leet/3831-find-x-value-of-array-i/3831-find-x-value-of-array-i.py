class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # subarray containing only num
            new_dp[num % k] += 1

            # extend every subarray ending at previous position
            for r in range(k):
                new_r = (r * num) % k
                new_dp[new_r] += dp[r]

            # all these are valid subarrays
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result