class Solution:
    def countSubstrings(self, s: str) -> int:

        # DP TAB 
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        res = 0 

        for g in range(n):
            for i in range(n-g):
                j = i + g 

                if s[i]==s[j] and (g<=2 or dp[i+1][j-1]==1):
                    dp[i][j] = 1 
                    res += 1 
        
        return res