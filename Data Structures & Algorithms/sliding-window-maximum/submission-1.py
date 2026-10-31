class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = -1
        q = deque()
        res = []

        for r in range(len(nums)):

            if q and q[0]<l+1:
                q.popleft()

            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)

            if r>=k-1:
                res.append(nums[q[0]])
                l+=1
        
        return res





