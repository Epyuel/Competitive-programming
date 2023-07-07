# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l_pointer=1
        r_pointer=n

        while l_pointer<=r_pointer:
            mid=(l_pointer+r_pointer)//2

            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                l_pointer=mid+1
            else:
                r_pointer=mid-1
