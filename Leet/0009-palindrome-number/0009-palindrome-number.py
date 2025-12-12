class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []

        n = x
        while n != 0:
            digits.append(n % 10)  # last digit
            n //= 10               # remove last digit

        return digits == digits[::-1]