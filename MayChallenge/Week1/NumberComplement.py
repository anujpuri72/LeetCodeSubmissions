class Solution:
    def findComplement(self, n: int) -> int:
        x = int(math.log(n, 2))
        m = 1 << x
        m = m | m - 1
        n = n ^ m
        return n
