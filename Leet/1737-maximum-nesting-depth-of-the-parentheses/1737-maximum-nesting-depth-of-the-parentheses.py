class Solution:
    def maxDepth(self, s: str) -> int:
        par = 0
        mx = 0
        for c in s:
            if c == "(":
                par += 1
            elif c == ")":
                mx = max(mx, par)
                par -= 1
        return mx
            