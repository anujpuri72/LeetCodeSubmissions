class Solution:
    def countSquares(self, nums: List[List[int]]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if(nums[i][j] == 0):
                    continue
                if((i == 0) or (j == 0)):
                    res += 1
                    continue
                nums[i][j] += min(nums[i-1][j], nums[i-1][j-1], nums[i][j-1])
                res += nums[i][j]
        return res
