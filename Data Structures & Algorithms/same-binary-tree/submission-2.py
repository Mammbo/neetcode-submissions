# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # for this problem i am going to use bfs as i need to make sure by level they are the same trees
        queue_p = deque([p])
        queue_q = deque([q])
    
        while queue_p and queue_q:
            if len(queue_p) != len(queue_q):
                return False
            current_len = len(queue_p)
            for i in range(current_len):
                node_p = queue_p.popleft()
                node_q = queue_q.popleft()
                if node_p is None and node_q is None:
                    continue

                if node_p is None or node_q is None or node_p.val != node_q.val:
                    return False
                queue_p.append(node_p.left)
                queue_q.append(node_q.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.right)
        return True
                        




        