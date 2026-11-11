class Solution:
    def numDecodings(self, s: str) -> int:

        # TAB DP O(1) space

        n = len(s)
        one = 1


        for i in range(n-1,-1,-1):
            res = 0 
            if s[i]!='0':
                res += one
            # else:
            #     res = 0

            if ((i+1<len(s)) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456')):
                res += two
            tmp = one
            one = res
            two = tmp

        return res



        


     
        