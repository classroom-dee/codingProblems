# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        
        # p_q, q_q = deque([p]), deque([q])

        # while p_q and q_q:
        #     p_curr, q_curr = p_q.popleft(), q_q.popleft()

        #     if (p_curr is None and q_curr) or (p_curr and q_curr is None):
        #         return False

        #     if p_curr is None and q_curr is None:
        #         continue

        #     if p_curr.val != q_curr.val:
        #         return False

        #     p_q.append(p_curr.left)
        #     p_q.append(p_curr.right)
        #     q_q.append(q_curr.left)
        #     q_q.append(q_curr.right)
        
        # return True

        # Simpler
        queue = deque([(p, q)])

        while queue:
            a, b = queue.popleft()

            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            queue.append((a.left, b.left))
            queue.append((a.right, b.right))

        return True