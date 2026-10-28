class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []
        total = 0 


        def dfs(i):

            nonlocal total
            if target==total:
                res.append(curr.copy())
                return 

            if total>target or i==len(nums):
                return 

            curr.append(nums[i])
            total+=nums[i]
            dfs(i) 
            curr.pop()
            total-=nums[i]

            dfs(i+1)

        dfs(0)
        return res


                
                
        