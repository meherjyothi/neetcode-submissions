class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        hs = set()
        res, curr = 0, 0  
        l = 0


        for i in range(n):
            while s[i] in hs:
                hs.remove(s[l])
                curr-=1
                l+=1

            if s[i] not in hs:
                hs.add(s[i])
                curr+=1
                res = max(res, curr)

                    
        return res
                



        