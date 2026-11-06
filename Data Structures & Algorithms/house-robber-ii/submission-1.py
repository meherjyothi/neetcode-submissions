class Solution:
    def rob(self, nums: List[int]) -> int:

        #MEM 
        
        def rec(i, arr, nums):
            if i>=len(nums):
                return 0


            if arr[i]:
                return arr[i]
            
            arr[i] = max(rec(i+2, arr, nums) + nums[i], rec(i+1, arr, nums))
            return arr[i]

        if len(nums)==1:
            return nums[0]
        return max(rec(0, [0]*(len(nums)-1), nums[:-1]), rec(0, [0]*(len(nums)-1), nums[1:]))

        




        