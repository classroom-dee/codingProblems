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
        # from itertools import permutations

        # valid = set()

        # for a, b, c in permutations(digits, 3):
        #     if a != 0 and c % 2 == 0:
        #         valid.add(a * 100 + b * 10 + c)

        # return len(valid)

        # But that was O(n3) so
        freq = [0] * 10

        for d in digits:
            freq[d] += 1

        count = 0

        for a in range(1, 10):      # hundreds: can't be 0
            for b in range(10):     # tens
                for c in range(0, 10, 2):  # ones: must be even
                    needed = [0] * 10
                    needed[a] += 1
                    needed[b] += 1
                    needed[c] += 1

                    if all(needed[d] <= freq[d] for d in range(10)):
                        count += 1

        return count
