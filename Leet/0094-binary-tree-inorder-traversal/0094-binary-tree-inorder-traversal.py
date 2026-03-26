# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def _traverse(node: Optional[TreeNode]):
            """
            Left -> Record -> Right
            """
            if not node:
                return result

            _traverse(node.left)
            result.append(node.val)
            _traverse(node.right)

        result = []
        _traverse(root)
        return result
