# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def _search(left, right):
            if not left and not right:
                return True

            if (left and not right) or (not left and right):
                return False

            if left.val == right.val:
                res_1 = _search(left.left, right.right)
                res_2 = _search(left.right, right.left)
                return res_1 and res_2
            else:
                return False
        
        res = _search(root.left, root.right)
        return res