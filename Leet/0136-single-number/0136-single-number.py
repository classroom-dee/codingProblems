class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # from collections import Counter

        if len(nums) == 1:
            return nums[0]

        # cnt = Counter({})
        # for n in nums:
        #     cnt.update({n})
        # return min(cnt, key=lambda x: cnt[x])

        # that was O(n) but used extra space
        # using the commutative + associative properties of bit ops

        rec = 0
        for n in nums:
            # print(f"{rec}({bin(rec)}) ^ {n}({bin(n)}) is {rec ^ n}({bin(rec ^ n)})")
            rec ^= n
        return rec
        