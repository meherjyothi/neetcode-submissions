# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxx = 0  
        def helper(root):
            nonlocal maxx
            if root==None:
                return 0 


            l, r = helper(root.left), helper(root.right)
            h =  max(l,r)+1
            d = l+r

            maxx = max(maxx, d)
            return h
            
        helper(root)
        return maxx