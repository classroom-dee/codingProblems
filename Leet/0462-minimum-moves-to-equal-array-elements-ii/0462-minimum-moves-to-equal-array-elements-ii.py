class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # using median + quick select
        def quick_select(arr, k):
            pivot = arr[len(arr)//2]

            left, equal, right = [], [], []

            for x in arr:
                if x > pivot:
                    right.append(x)
                elif x < pivot:
                    left.append(x)
                else:
                    equal.append(x)

            if k <= len(left):
                return quick_select(left, k)
            elif k <= len(left) + len(equal):
                return pivot
            else:
                return quick_select(right, k - len(left) - len(equal))
        
        target = quick_select(nums, len(nums)//2 + 1)

        # # using median + python sort
        # nums.sort()
        # target = nums[len(nums) // 2]

        # # using mean
        # mean = sum(nums) / len(nums)
        # min_dev = float("inf")
        # for n in nums:
        #     min_dev = min(abs(n - mean), min_dev)
        
        # target = 0
        # for n in nums:
        #     if abs(n - mean) == min_dev:
        #         target = n
        #         break
        
        moves = 0 
        for n in nums:
            moves += abs(n - target)
        
        return moves
        
