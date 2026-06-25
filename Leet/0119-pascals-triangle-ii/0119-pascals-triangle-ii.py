class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # index 0 is already handled
        prev = [0, 1, 0]
        for i in range(rowIndex):
            new_one = []
            for j in range(len(prev) - 1):
                new_one.append(prev[j] + prev[j+1])
            prev = [0] + new_one + [0]
        
        return prev[1:-1]