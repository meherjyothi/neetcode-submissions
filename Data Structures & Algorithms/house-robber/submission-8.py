class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #BOTTOM UP DP w arr 
        res = 0 
        n = len(nums)
        arr = [0]*n

        arr[n-1] = nums[n-1]
        arr[n-2] = max(nums[n-1], nums[n-2])
        for i in range(n-3, -1, -1):
            arr[i] = max(nums[i]+arr[i+2], arr[i+1])

        return arr[0]

