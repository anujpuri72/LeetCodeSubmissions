class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = {}
        for i in nums:
            r[i] = r.get(i, 0)+1
        return ([k for k, v in sorted(r.items(), key=lambda item: item[1], reverse=True)][0])
