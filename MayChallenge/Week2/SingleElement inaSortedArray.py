class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
