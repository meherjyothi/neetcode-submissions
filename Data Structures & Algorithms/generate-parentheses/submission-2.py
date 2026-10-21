class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        curr = ""
        def helper(o, c, curr):
            if o==n and c==n:
                res.append(str(curr))
                return 

            if o<n:
                helper(o+1, c, curr+"(")

            
            if c<o and c<n:
                helper(o, c+1, curr+")")

        helper(0, 0, "")
        return res


        