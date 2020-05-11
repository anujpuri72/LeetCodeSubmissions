class Solution:
    def firstUniqChar(self, s: str) -> int:
        r = {}
        if (s == ""):
            return -1
        for i in s:
            r[i] = [r.get(i, [0, 0])[0] + 1, s.index(i)]
        b = sorted(r.items(), key=lambda x: x[1])
        if (b[0][1][0] == 1):
            return b[0][1][1]
        else:
            return -1
