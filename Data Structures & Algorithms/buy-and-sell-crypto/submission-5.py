class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n==0:
            return 0
        minn = prices[0]
        res = 0 
        for i in range(n):
            minn = min(minn, prices[i])
            res = max(res, prices[i]-minn)
        if res<0:
            res = 0

        return res


        