# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        if not root:
            return 0

        q = deque([(root, 0)])
        while q:
            curr, depth = q.popleft()
            depth += 1

            l = curr.left
            r = curr.right
            
            if not l and not r:
                return depth
            
            if l:
                q.append((l, depth))
            if r:
                q.append((r, depth))
            
            