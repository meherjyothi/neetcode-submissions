class Solution:
    def minWindow(self, s: str, t: str) -> str:

        l, r = 0, 0 
        hms, hmt = {}, {}
        res = [-1,-1]
        resLen = float("inf")

        if len(s)<len(t):
            return ""

        for i in range(len(t)):
            hmt[t[i]] = hmt.get(t[i], 0) + 1

        have, need = 0, len(hmt) 




        while r<len(s):

            hms[s[r]] = hms.get(s[r], 0) + 1

            if s[r] in hmt and hms[s[r]]==hmt[s[r]]:
                have+=1

            while have==need:
                
                if r-l+1 < resLen:
                    res = [l,r]
                    resLen = r-l+1

                hms[s[l]] -=1 

                if s[l] in hmt and hms[s[l]]<hmt[s[l]]:
                    have-=1

                l+=1

            r+=1

        l, r = res
        return s[l:r+1] if resLen!=float("inf") else ""

 

            


        