class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for i in range(1, len(columnTitle) + 1):
            digit = (ord(columnTitle[-i]) - 64)
            res += (26 ** (i - 1)) * digit
        
        return res