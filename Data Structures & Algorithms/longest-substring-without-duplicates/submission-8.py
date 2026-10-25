class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        ## V OPTIMAL

        hm = defaultdict()

        l, r = 0, 0
        res = 0

        while r<len(s):
            if s[r] not in hm or (s[r] in hm and l>hm[s[r]]):
                res = max(res, r-l+1)
                hm[s[r]] = r 
                r+=1
            else:
                l = hm[s[r]] + 1 
        
        return res


                





        return res



            
            
        