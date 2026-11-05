class Solution:
    def climbStairs(self, n: int) -> int:

        # bottom up + without arr 

        if n<=3:
            return n 
        one, two, total = 1, 1, 0
        for i in range(n-1):
            total = one + two 
            temp = one 
            one = total 
            two = temp

        return total


            



        