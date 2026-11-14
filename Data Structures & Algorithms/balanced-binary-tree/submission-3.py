# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = True 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True 
        def helper(root):
            nonlocal res

            if root==None:
                return 0 

            lh = helper(root.left)
            rh = helper(root.right)
            if not (res==True and abs(lh-rh)<=1 ):
                res = False

            return max(lh, rh) + 1 

        helper(root)
        return res

    
        