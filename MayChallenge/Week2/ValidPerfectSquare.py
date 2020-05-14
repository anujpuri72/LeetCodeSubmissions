import math


class Solution:
    #     def sieveOfEratosthenes(self,N, s):
    #         prime = [False] * (N+1)

    #         for i in range(2, N+1, 2):
    #             s[i] = 2

    #         for i in range(3, N+1, 2):
    #             if (prime[i] == False):
    #                 s[i] = i

    #                 for j in range(i, int(N / i) + 1, 2):
    #                     if (prime[i*j] == False):
    #                         prime[i*j] = True
    #                         s[i * j] = i
    def isPerfectSquare(self, N: int) -> bool:
        if(N == 1):
            return True
        i = 2
        while(i*i <= N):
            if(i*i == N):
                return True
            i += 1
        return False

#         s = [0] * (N+1)

#         self.sieveOfEratosthenes(N, s)

#         curr = s[N]

#         cnt = 1

#         while (N > 1):
#             N //= s[N]

#             if (curr == s[N]):
#                 cnt += 1
#                 continue
#             if(cnt&1):
#                 return False

#             curr = s[N]
#             cnt = 1
#         return True
