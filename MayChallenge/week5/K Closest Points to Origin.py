import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l = []
        for i in points:
            l.append((i[0], i[1], math.sqrt(i[0]*i[0] + i[1]*i[1])))
        l.sort(key=lambda x: x[2])
        s = []
        for i in range(K):
            s.append([l[i][0], l[i][1]])
        return s
