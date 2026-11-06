class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # MEM 
        arr = [0]*len(cost)

        def dfs(i):

            if i>=len(cost):
                return 0

            if arr[i]:
                return arr[i]

            arr[i] =  min(dfs(i+1), dfs(i+2)) + cost[i]
            return arr[i]


        return min(dfs(0), dfs(1))


        