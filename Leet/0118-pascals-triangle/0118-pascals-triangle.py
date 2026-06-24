class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res = []
        # for i in range(numRows):
        #     if i == 0:
        #         res.append([1])
        #         continue
            
        #     row = []
        #     for j in range(len(res[i-1]) + 1):
        #         if j == 0:
        #             row.append(1)
        #         elif j == len(res[i-1]):
        #             row.append(1)
        #         else:
        #             row.append(res[i-1][j-1] + res[i-1][j])
            
        #     res.append(row)
        # return res

        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                # handles the padding too
                prev = [0] + res[-1] + [0]
                res.append([prev[j] + prev[j+1] for j in range(len(prev)-1)])
        return res