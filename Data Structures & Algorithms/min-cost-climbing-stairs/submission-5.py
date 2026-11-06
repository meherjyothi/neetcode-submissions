class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # BOTTOM UP 
        n = len(cost)
        arr = [0]*n

        arr[n-1] = cost[n-1]
        arr[n-2] = cost[n-2]

        for i in range(n-3, -1, -1):
            arr[i] = cost[i] + min(arr[i+1], arr[i+2])
        
        return min(arr[0], arr[1])






        