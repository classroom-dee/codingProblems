class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Naive-ish recurse
        # def play(arr):
        #     # only one stone left
        #     if len(arr) == 1:
        #         return 0

        #     best_diff = float("-inf")

        #     # choose range
        #     for x in range(2, len(arr) + 1):
        #         this = sum(arr[:x])

        #         new_arr = [this] + arr[x:]

        #         # the opponent plays optimally
        #         # = opponent's advantage
        #         other_diff = play(new_arr)

        #         # this player's advantage = 
        #         # what this player scores - opponent's advantage
        #         this_diff = this - other_diff

        #         best_diff = max(best_diff, this_diff)

        #     return best_diff
        # return play(stones)
        
        # DP solution
        pref_run = 0
        prefix = [
            (pref_run := pref_run + s)
            for s in stones
        ]
        # this is O(n**2)
        # prefix = [sum(stones[:i+1]) for i in range(len(stones))]
        dp = [0] * len(stones)
        dp[-1] = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            dp[i] = max(
                dp[i + 1],
                prefix[i] - dp[i + 1]
            )
        
        return dp[1]