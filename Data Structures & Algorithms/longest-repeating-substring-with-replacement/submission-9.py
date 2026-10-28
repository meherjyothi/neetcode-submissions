class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0, 0 
        hm = {}
        res = 0 
        mfk, mfv = -1, -1

        for r in range(len(s)):

            hm[s[r]] = hm.get(s[r], 0) + 1 
            if hm.get(s[r]) > mfv:
                mfv = hm.get(s[r])
                mfk = hm[s[r]]

            if r-l+1 - mfv > k:
                if hm[s[l]]>1:
                    hm[s[l]] -= 1  
                else:
                    del hm[s[l]]
                l+=1

            else:
                res = max(res, r-l+1)

        return res



        