class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1, count2 = [0]*26, [0]*26 

        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')] += 1
            count2[ord(s2[i])-ord('a')] += 1

        if count1==count2:
            return True

        l, r = 0, len(s1)
        while r<len(s2):


            count2[ord(s2[l])-ord('a')] -= 1 
            count2[ord(s2[r])-ord('a')] += 1 #conf
            l+=1
            r+=1

            if count1==count2:
                return True


        return False

            


         
        