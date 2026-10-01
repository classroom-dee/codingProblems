class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        seq = []
        
        for c in s:
            if c in dic:
                seq.append(dic[c])
            else:
                if not seq or c != seq[-1]:
                    return False
                seq.pop()

        return not seq