class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean = "".join(c for c in s if c.isalnum()).lower()
        # reverse = clean[::-1]
        # return clean == reverse

        # OR
        import re
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reverse = clean[::-1]
        return clean == reverse