# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = deque()
        if not root:
            return []
        q.append(root)

        ans = []

        while q:
            level = []
            for _ in range(len(q)):
                popped = q.popleft()
                level.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            ans.append(level[-1])
        
        return ans

            
                
        