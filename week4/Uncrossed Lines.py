class Solution:
    def subsequence(self, A, B, i, j, dp):
        # print(i,j)
        if(i == len(A) or j == len(B)):
            return 0
        elif dp[i][j] != -1:
            return dp[i][j]
        elif(A[i] == B[j]):
            dp[i][j] = 1+self.subsequence(A, B, i+1, j+1, dp)
        else:
            dp[i][j] = max(self.subsequence(A, B, i, j+1, dp),
                           self.subsequence(A, B, i+1, j, dp))
        return dp[i][j]

    def maxUncrossedLines(self, A1: List[int], B1: List[int]) -> int:
        dp = [[-1]*(len(B1) + 1) for _ in range(len(A1) + 1)]
        return self.subsequence(A1, B1, 0, 0, dp)
