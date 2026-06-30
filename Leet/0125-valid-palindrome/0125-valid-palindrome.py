class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean = "".join(c for c in s if c.isalnum()).lower()
        # reverse = clean[::-1]
        # return clean == reverse

        # # OR
        # import re
        # clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # reverse = clean[::-1]
        # return clean == reverse

        # Two pointers approach
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True