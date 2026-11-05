class Solution:
    def climbStairs(self, n: int) -> int:

        # memo 

        arr = [0]*n

        def rec(i, res):
            if i>n:
                return 0
            if i==n:
                res += 1 
                return res
            if arr[i]:
                return arr[i]
            arr[i] = rec(i+1, res) + rec(i+2, res)
            return arr[i]
        
        return rec(0, 0)



        