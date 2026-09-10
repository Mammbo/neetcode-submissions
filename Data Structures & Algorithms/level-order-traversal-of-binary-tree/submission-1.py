# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: 
            return []
        # level order is just bfs 
        ans = []
        queue = deque([root])
        while queue: 
            curr_len = len(queue)
            ans_append = []
            for i in range(curr_len):
                node = queue.popleft()

                ans_append.append(node.val)

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            ans.append(ans_append)
        return ans
        
        