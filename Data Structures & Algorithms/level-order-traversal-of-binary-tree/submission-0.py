# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # this is literally just bfs
        # i want to return the level order traversal of the tree and return a list of list to it
        if root is None: 
            return []
        res = []

        queue = deque([root])

        while queue:
            curren_len = len(queue)
            append_res = []
            for _ in range(curren_len):
                node = queue.popleft()
                append_res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            res.append(append_res)
        return res
                


        