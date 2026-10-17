# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if p==None or q==None:
                if p!=None or q!=None:
                    return False
                return True

            return dfs(p.left, q.left) and dfs(p.right, q.right) and p.val==q.val

        return dfs(p,q)

        