class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        i = 0
        count = 0
        gcount = 0
        l = {0: -1}
        while(i < len(nums)):
            count += 1 if(nums[i] == 1) else -1
            if(count in l.keys()):
                gcount = max(gcount, i-l[count])
            else:
                l[count] = i
            i += 1
        return gcount
