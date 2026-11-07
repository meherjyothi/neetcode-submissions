class Solution:
    def longestPalindrome(self, s: str) -> str:

        # DP [][]
        n = len(s)
        res = ""
        resLen = 0 

        dp = [[0]*n for _ in range(n)]

        #FOR CONDITINS TRICKY
        for g in range(n):
            for i in range(0, n-g):
                j = g + i 
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]==1):
                    dp[i][j] = 1
                    if j-i+1>resLen:
                        resLen = j-i+1
                        res = s[i:j+1]
        return res
        


        
        