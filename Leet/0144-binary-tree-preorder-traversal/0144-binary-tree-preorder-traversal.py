# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def _search(node):
            if not node:
                return result

            result.append(node.val)

            if node.left:
                _search(node.left)
            if node.right:
                _search(node.right)

        _search(root)
        return result