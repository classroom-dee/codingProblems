class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0
        for n1 in arr1:
            if all(abs(n1 - n2) > d for n2 in arr2):
                res += 1
        return res
        
        # res = []
        # for i, n1 in enumerate(arr1):
        #     for n2 in arr2:
        #         if not res: res.append(1)
        #         if len(res) < i + 1: res.append(1)
        #         res[i] = res[i] and abs(n1 - n2) > d
        
        # return sum(res)
        