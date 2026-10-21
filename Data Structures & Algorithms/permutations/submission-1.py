class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n==0:
            return [[]]
        for perm in self.permute(nums[1:]):
            for i in range(len(perm)+1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
        return res


                

        