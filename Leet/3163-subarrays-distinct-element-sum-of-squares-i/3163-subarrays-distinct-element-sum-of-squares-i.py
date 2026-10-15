class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # b4 = {}
        # s = 0
        # for i in range(len(nums)):
        #     if b4:
        #         b4.discard(nums[i-1])
        #     for j in range(i, len(nums)):
        #         if not b4:
        #             b4 = set(nums[i:j+1])
        #             s += len(b4) ** 2
        #             continue
        #         b4.add(nums[j])
        #         s += len(b4) ** 2
        
        # return s
        s = 0

        for i in range(len(nums)):
            seen = set()

            for j in range(i, len(nums)):
                seen.add(nums[j])
                s += len(seen) ** 2

        return s