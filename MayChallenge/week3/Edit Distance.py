class Solution:
    def subsequence(self, A, B, i, j, dp):
        if(dp[i][j] != -1):
            return dp[i][j]
        if(i == 0 or j == 0):
            dp[i][j] = max(i, j)
        elif(A[i-1] == B[j-1]):
            dp[i][j] = self.subsequence(A, B, i-1, j-1, dp)
        else:
            dp[i][j] = 1+min(self.subsequence(A, B, i, j-1, dp), self.subsequence(
                A, B, i-1, j, dp), self.subsequence(A, B, i-1, j-1, dp))
        return dp[i][j]

    def minDistance(self, A1: str, B1: str) -> int:
        dp = [[-1]*(len(B1) + 1) for _ in range(len(A1) + 1)]
        return self.subsequence(A1, B1, len(A1), len(B1), dp)
