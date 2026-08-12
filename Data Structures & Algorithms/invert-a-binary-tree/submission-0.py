# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # inverting a binary tree is a level order traversal 
        # that quite literally means to implement bfs
        # the starting input is the root of the tree
        if root is None: 
            return root
        
        queue = deque([root])

        while queue:
            # do something to the level
            current_len_queue = len(queue)
            for i in range(current_len_queue):
                node = queue.popleft()

                # do somethign to the node
                # at this point i can swap node.left and node.right

                node.left, node.right = node.right, node.left

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        return root

        # lets walk through a couple of examples, okay lets say i am given just the root, if root is empty return []
        # if it is just the root seems like my logic work 

        # now for 3 nodes

        #queue =[3]
        # curr len = 1
        # 0 --> 
        # node = 3
        # node.left = 2, node.right = 1
        # node.left = 1, node.right = 2
        # add them both to queue if they exist
        # continue from there 
        # they are both empty so it is null 


        