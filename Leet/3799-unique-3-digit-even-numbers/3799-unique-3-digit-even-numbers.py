class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # nums = set()
        # used = [False] * len(digits)

        # def backtrack(path):
        #     if len(path) == 3:
        #         if path[0] != 0 and path[-1] % 2 == 0:
        #             num = path[0] * 100 + path[1] * 10 + path[2]
        #             nums.add(num)
        #         return

        #     for i in range(len(digits)):
        #         if used[i]:
        #             continue

        #         used[i] = True
        #         path.append(digits[i])

        #         backtrack(path)

        #         path.pop()
        #         used[i] = False

        # backtrack([])
        # return len(nums)

        # For Python, this could be better
        from itertools import permutations

        valid = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                valid.add(a * 100 + b * 10 + c)

        return len(valid)