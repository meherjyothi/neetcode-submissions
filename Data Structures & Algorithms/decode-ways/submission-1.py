class Solution:
    def numDecodings(self, s: str) -> int:

        # MEM DP  
        count = 0 

        n = len(s)
        dp = [0]*n 

        def dfs(i):

            if i>=len(s):
                return 1

            if dp[i]:
                return dp[i]

            if s[i]=='0':
                return 0 

            res = dfs(i+1)

            if ((i+1<len(s)) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456')):
                res += dfs(i+2)

            dp[i] = res

            return res

        return dfs(0)



     
        