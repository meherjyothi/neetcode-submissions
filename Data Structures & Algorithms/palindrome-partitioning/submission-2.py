class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(curr):
            return curr == curr[::-1]
        
        ans = []
        res = []

        def dfs(i, curr):
            if i==len(s):
                if curr and isPal(curr):
                    ans.append(curr)
                    res.append(ans.copy())
                    ans.pop()
                    # curr = ""
                return 

            curr += s[i]

            if isPal(curr):
                ans.append(curr)
                dfs(i+1, "")
                ans.pop()

            dfs(i+1, curr)



        dfs(0, "")
        return res



        