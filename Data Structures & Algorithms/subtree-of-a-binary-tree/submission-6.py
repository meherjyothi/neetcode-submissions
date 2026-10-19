# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(r, sr):
            if r==None or sr==None:
                if r!=None or sr!=None:
                    return False
                return True
            return r.val==sr.val and sameTree(r.left, sr.left) and sameTree(r.right, sr.right) 

        if root==None:
            return False
        return sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)







        