class Solution:
    # def isValid(self, s: str) -> bool:
    #     # Base cases
    #     if s == "":
    #         return True

    #     if len(s) % 2 != 0: return False

    #     for i in range(len(s) - 1):
    #         if s[i] + s[i+1] in {"()", "[]", "{}"}:
    #             # Remove the matched pair and recurse
    #             reduced = s[:i] + s[i+2:]
    #             return self.isValid(reduced)

    #     # If no adjacent valid pair exists, it's invalid
    #     return False

    # def isValid(self, s: str) -> bool:
    #     prev = None
    #     while prev != s:
    #         prev = s
    #         s = s.replace("()", "").replace("[]", "").replace("{}", "")
    #     return s == ""

    # Fastest: stack approach
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                return False
        
        return not stack
