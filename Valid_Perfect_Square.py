class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l_pointer=1
        r_pointer=num

        while l_pointer<=r_pointer:
            mid=(l_pointer+r_pointer)//2

            if mid*mid == num:
                return True
            elif mid*mid < num:
                l_pointer=mid+1
            else:
                r_pointer=mid-1
        return False
