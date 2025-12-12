class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        is_even = target % 2 == 0
        half = target // 2
        halves = []

        for i, n in enumerate(nums):
            if is_even and n == half:
                halves.append(i)
            else:
                lookup[(n, target - n)] = i

                other_half = (target - n, n)
                if other_half in lookup:
                    return [lookup[other_half], i]
        else:
            # print()
            return halves
