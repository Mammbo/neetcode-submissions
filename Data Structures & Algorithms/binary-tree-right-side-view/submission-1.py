# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # return only the values of the tree visible from the right side
        # i could use dfs traversing only to the right and appending those nodes
        #i could also do a level order traversal and append the last element in the queue
        # lets do both

        if root is None: 
            return res
            
        queue = deque([root])

        while queue:
            current_len = len(queue)
            res.append(queue[-1].val)
            for _ in range(current_len):
                node = queue.popleft()

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        return res
                
