# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def find(root, target):
            if root==target:
                return True
            if root==None:
                return False
            return find(root.left, target) or find(root.right, target)

        if root==p or root==q:
            return root 
        if find(root.left, p) and find(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if find(root.right, p ) and find(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        if (find(root.left, p) and find(root.right, q)) or (find(root.left, q) and find(root.right, p)):
            return root 
        return TreeNode(None)





        