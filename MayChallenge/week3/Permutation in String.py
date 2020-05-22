class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        if(len(s) < len(p)):
            return False
        i = len(p)
        acheck = {}
        tocheck = {}
        for j in range(len(p)):
            acheck[p[j]] = acheck.get(p[j], 0)+1
            tocheck[s[j]] = tocheck.get(s[j], 0)+1
        if(acheck == tocheck):
            return True
        while (i < len(s)):
            tocheck[s[i]] = tocheck.get(s[i], 0)+1
            tocheck[s[i-len(p)]] = tocheck[s[i-len(p)]] - 1
            if(tocheck[s[i-len(p)]] == 0):
                del tocheck[s[i-len(p)]]
            if(acheck == tocheck):
                return True
            i += 1
        return False
