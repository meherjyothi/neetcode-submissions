class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0 
        hm = {}
        res = 0 
        maxf = 0 

        for r in range(len(s)):

            hm[s[r]] = hm.get(s[r], 0) + 1 
            maxf = max(maxf, hm[s[r]])

            if r-l+1 - maxf > k:
                if hm[s[l]]>1:
                    hm[s[l]] -= 1  
                else:
                    del hm[s[l]]
                l+=1

            else:
                res = max(res, r-l+1)

        return res



        