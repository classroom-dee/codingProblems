class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = [''] * len(max(strs, key=lambda s: len(s)))
        if not arr: return ''

        for s in strs:
            if not s: return ''
            for i, c in enumerate(s):
                arr[i] += c
        
        res = ''
        length = len(arr[0])
        for ls in arr:
            ls_set = set(ls)
            if len(ls_set) == 1 and len(ls) == length:
                res += ls[0]
            else: break
        
        return res