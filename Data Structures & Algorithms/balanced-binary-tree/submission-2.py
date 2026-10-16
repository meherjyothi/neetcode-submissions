# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root==None:
                return [True, 0]
            
            lft, rht = dfs(root.left), dfs(root.right)
            return [((abs(lft[1] - rht[1])<=1) and lft[0] and rht[0]), 1+max(lft[1],rht[1])]
        
        return dfs(root)[0]

            
            
        