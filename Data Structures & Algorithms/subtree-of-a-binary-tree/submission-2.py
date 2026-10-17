# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        res = False
        def dfs(p, q):
            if p==None: #q?
                return 

            
            if p.val==q.val:
                if helper(p,q)==True:
                    nonlocal res
                    res=True

            
            dfs(p.left, q)
            dfs(p.right, q)
            return 

        def helper(p, q):
            if q==None or p==None:
                if p!=None or q!=None:
                    return False
                return True

            return helper(p.left, q.left) and helper(p.right, q.right) and p.val==q.val
            
        dfs(root, subRoot)
        return res
        