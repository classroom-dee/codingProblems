class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = {} # that's O(n)
        # for num in nums:
        #     d.setdefault(num, 0)
        #     d[num] += 1
        #     if d[num] > len(nums) / 2:
        #         return num

        # use voting algo
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate