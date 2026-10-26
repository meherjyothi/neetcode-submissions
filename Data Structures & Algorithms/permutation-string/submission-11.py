class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1)>len(s2):
            return False
        l, r = 0, len(s1)
        hm1, hm2 = defaultdict(), defaultdict()
        for i in range(len(s1)):
            hm1[s1[i]] = hm1.get(s1[i], 0) + 1
            hm2[s2[i]] = hm2.get(s2[i], 0) + 1
        if hm1==hm2:
            return True


        while r<len(s2):
            #is this valid compar?
            
            hm2[s2[l]] -= 1 
            if hm2[s2[l]]==0:
                hm2.pop(s2[l])
            hm2[s2[r]] = hm2.get(s2[r], 0) + 1

            if hm1==hm2:
                return True

            l+=1
            r+=1



        return False


        