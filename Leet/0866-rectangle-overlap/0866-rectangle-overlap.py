class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # cases that exclude eachother
        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[1] >= rec2[3] or rec2[1] >= rec1[3])