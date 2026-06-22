# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # from collections import deque

        # if not root:
        #     return False
        
        # q = deque([(root, root.val)])
        # while q:
        #     curr, total = q.popleft()

        #     if not curr.left and not curr.right and total == targetSum:
        #         return True

        #     if curr.left:
        #         q.append((curr.left, total + curr.left.val))
        #     if curr.right:
        #         q.append((curr.right, total + curr.right.val))
        # else:
        #     return False

        # # OR recursively
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        diff = targetSum - root.val

        return self.hasPathSum(root.left, diff) or self.hasPathSum(root.right, diff)