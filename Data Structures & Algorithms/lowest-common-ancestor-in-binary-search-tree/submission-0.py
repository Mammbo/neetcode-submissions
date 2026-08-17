# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # immedietly i know to traverse using the bst conditions 
        # if there is only two nodes
        # it will be the one that is a descendant of itself
        # so i guess there are three cases 
        # one p < root and q > root or vice versa
        # if this was true return the root

        # if both p and q < root:
        # traverse left 
        # compare the children of that node 
        # if the first case or one of the values is equal to it return the root
        # if second case repeat

        if (p.val <= root.val <= q.val) or (p.val >= root.val >= q.val):
            return root

        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        else: 
           return self.lowestCommonAncestor(root.right, p, q)
        