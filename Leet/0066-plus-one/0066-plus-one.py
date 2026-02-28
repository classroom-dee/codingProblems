class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # That's buggy
        # i = len(digits) - 1
        # next_add = 1
        # curr = digits[-1]
        # while i > -1:
        #     if curr + next_add == 10:
        #         digits[i] = 0
        #         next_add = 1
        #     else:
        #         digits[i] = curr + next_add
        #         next_add = 0
            
        #     curr = digits[i - 1]
        #     i -= 1
        # return [1] + digits if digits[0] == 0 else digits

        i = len(digits) - 1

        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            i -= 1

        return [1] + digits