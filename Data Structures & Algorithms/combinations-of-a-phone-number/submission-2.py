class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        hm = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []


        def dfs(i, curr):
            if i==len(digits):
                if curr:
                    res.append(curr)
                return 
            
            for ch in hm[digits[i]]:
                curr+=ch
                dfs(i+1, curr)
                curr=curr[:-1]
            return 

        dfs(0, "")
        return res

