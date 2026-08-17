# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # i am given two binary trees
        # one of root and one of subroot
        # return true if there is a subtree of subroot in root false otherwise 

        # this is similar to another dfs problem of comparing if two trees are the same i canuse that logic in this problem
        if not subRoot: 
            return True
        if not root: 
            return False
        
        if self.sameTree(root, subRoot): 
            return True
        return(self.isSubtree(root.left, subRoot) or  
                self.isSubtree(root.right, subRoot))


    def sameTree(self, root, subroot):
        if not subroot and not root: 
            return True
        if subroot and root and root.val == subroot.val:                
            return (self.sameTree(root.left, subroot.left) and self.sameTree(root.right, subroot.right))
        return False

                
            