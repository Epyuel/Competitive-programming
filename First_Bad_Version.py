# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l_pointer,r_pointer,mid=1,n,1

        while l_pointer <= r_pointer:
            mid=(l_pointer + r_pointer)//2
            if isBadVersion(mid):
                r_pointer=mid-1
            else:
                l_pointer=mid+1
        
        return max(mid,l_pointer)
