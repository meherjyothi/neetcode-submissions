class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hm = {}

        l, r = 0, 0
        curr = 0 
        res = 0

        while r<len(s):

            if s[r] in hm and hm[s[r]]>0:
                hm[s[l]] -=1 
                l+=1
                curr-=1
            
            else:
                if s[r] in hm:
                    hm[s[r]] += 1
                else:
                    hm[s[r]] = 1 
                r+=1
                curr+=1
                res = max(res, curr)

        return res



            
            
        