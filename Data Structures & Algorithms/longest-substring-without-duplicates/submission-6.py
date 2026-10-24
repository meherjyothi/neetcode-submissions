class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hs = set()

        l, r = 0, 0
        curr = 0 
        res = 0

        while r<len(s):

            if s[r] in hs:
                hs.remove(s[l]) 
                l+=1
                curr-=1
            
            else:
                hs.add(s[r])
                r+=1
                curr+=1
                res = max(res, curr)

        return res



            
            
        