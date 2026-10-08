class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 0
        primitive = []
        shell_removed = []
        for c in s:
            if c == "(":
                open += 1
            else:
                open -= 1
            
            primitive.append(c)
            if open == 0:
                shell_removed += primitive[1:-1]
                primitive = []

        return "".join(shell_removed)
                