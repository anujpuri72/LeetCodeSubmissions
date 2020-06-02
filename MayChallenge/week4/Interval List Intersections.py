class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a = 0
        b = 0
        l = []
        while(a < len(A)and b < len(B)):
            if(B[b][0] <= A[a][1] and B[b][1] >= A[a][0]):
                l.append([max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
            if(B[b][1] > A[a][1]):
                a += 1
            else:
                b += 1
        return(l)
