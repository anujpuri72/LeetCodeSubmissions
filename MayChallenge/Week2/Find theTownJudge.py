class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        res = {}
        maxcount = 0
        max_var = ""
        if(N == 1):
            return 1
        for i in trust:
            res[i[1]] = res.get(i[1], 0)+1
            if(res[i[1]] > maxcount):
                maxcount = res[i[1]]
                max_var = i[1]
        if(maxcount != N-1):
            return -1
        for i in trust:
            if (i[0] == max_var):
                return -1
        return max_var
