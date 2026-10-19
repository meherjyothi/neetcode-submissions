# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(root, maxx):
            if root==None:
                return 0
            maxx = max(maxx, root.val)
            if root.val>=maxx:
                return 1+helper(root.left, maxx)+helper(root.right, maxx)
            return helper(root.left, maxx)+helper(root.right, maxx)

        return helper(root, root.val)

        
            