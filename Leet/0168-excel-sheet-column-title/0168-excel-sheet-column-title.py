class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        import string
        # lc = len(string.ascii_uppercase) # letters count
        
        # if columnNumber <= lc:
        #     return string.ascii_uppercase[columnNumber - 1]

        result = ''
        # while columnNumber >= lc:
        #     div = int(columnNumber / lc)
        #     rem = columnNumber % lc
        #     result = string.ascii_uppercase[rem - 1] + result
        #     columnNumber = div
        #     if columnNumber <= lc:
        #         result = string.ascii_uppercase[columnNumber - 1] + result
        #         break
        while columnNumber > 0:
            columnNumber -= 1
            result = string.ascii_uppercase[columnNumber % 26] + result
            columnNumber //= 26
        return result