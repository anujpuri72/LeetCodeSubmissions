class Solution:
    def firstBadVersion(self, n):
        low=1
        high=n
        mid=int((low+high)//2)
        while (low<=high):
            mid=int((low+high)//2)
            if(isBadVersion(mid)==True and isBadVersion(mid-1)==False):
                return mid
            elif(isBadVersion(mid)==False):
                    low=mid+1
            else :
                high=mid-1