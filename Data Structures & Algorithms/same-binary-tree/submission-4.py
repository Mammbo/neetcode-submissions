# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # i am given two roots of two binary trees p and q 
        # i must return true if the trees are equivalent otherwise false 
        # they must share the same strucutre and same node values 
        # i can do a depth first search

        def sameTree(p, q):
            if not p and not q: 
                return True
            
            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            return False
        return sameTree(p, q)
        