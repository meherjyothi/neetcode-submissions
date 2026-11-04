class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols, pos, neg = set(), set(), set()
        mat = [['.']*n for _ in range(n)]
        res = []

        def dfs(i, j, cols, pos, neg, mat):
            if i==n:
                copy = ["".join(row) for row in mat]
                res.append(copy)
                return 



            for j in range(n): 
                if (j  in cols or i+j in pos or i-j in neg or j>=n):
                    continue
                cols.add(j)
                pos.add(i+j)
                neg.add(i-j)
                mat[i][j] = 'Q'
                dfs(i+1, j, cols, pos, neg, mat)

                cols.remove(j)
                pos.remove(i+j)
                neg.remove(i-j)
                mat[i][j] = '.'

            return 

        dfs(0, 0, cols, pos, neg, mat)
        return res


        