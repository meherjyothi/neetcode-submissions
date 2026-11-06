class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #TOP DOWN MEM DP
        res = 0 
        n = len(nums)
        arr = [0]*n

        def dfs(i):
            if i>=len(nums):
                return 0
            if arr[i]:
                return arr[i]
            
            arr[i] = max(dfs(i+2) + nums[i], dfs(i+1))
            return arr[i]

        return dfs(0)
