# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0

        def dfs(node):
            nonlocal result

            if not node:
                return 0, 0  # sum, count

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            subtree_sum = left_sum + right_sum + node.val
            subtree_count = left_count + right_count + 1

            if subtree_sum // subtree_count == node.val:
                result += 1

            return subtree_sum, subtree_count

        dfs(root)
        return result