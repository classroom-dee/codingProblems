class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # # Naive
        # needle_len = len(needle)
        # for i in range(len(haystack) - needle_len + 1):
        #     if haystack[i:i+needle_len] == needle:
        #         return i
        # else:
        #     return -1

        # # -------------- -------------- --------------
        # # OR, Boyer-Moore
        # bad_char = {}
        # for i, c in enumerate(needle):
        #     bad_char[c] = i

        # i = 0
        # while i <= len(haystack) - len(needle):
        #     j = len(needle) - 1
        #     while j >= 0 and needle[j] == haystack[i + j]:
        #         j -= 1
        #     if j < 0:
        #         return i
        #     shift = j - bad_char.get(haystack[i + j], -1)
        #     i += max(1, shift)

        # return -1

        # # -------------- -------------- --------------
        # # OR, KMP
        # # Build LPS array
        # lps = [0] * len(needle)
        # j = 0
        # for i in range(1, len(needle)):
        #     while j > 0 and needle[i] != needle[j]:
        #         j = lps[j - 1]
        #     if needle[i] == needle[j]:
        #         j += 1
        #         lps[i] = j
        # # Search
        # j = 0
        # for i in range(len(haystack)):
        #     while j > 0 and haystack[i] != needle[j]:
        #         j = lps[j - 1]
        #     if haystack[i] == needle[j]:
        #         j += 1
        #     if j == len(needle):
        #         return i - j + 1

        # return -1

        # # -------------- -------------- --------------
        # # But in Python,
        return haystack.find(needle) # CPython, fastsearch