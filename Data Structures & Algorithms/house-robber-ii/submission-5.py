class Solution:
    def rob(self, nums: List[int]) -> int:

        #BOTTOM UP 
        
        def helper(nums):
            rob1, rob2 = 0, 0 

            for num in nums:
                rob = max(num + rob1, rob2)
                rob1 = rob2  
                rob2 = rob 
            return rob2


        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))

        




        