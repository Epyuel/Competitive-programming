class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==1:
            return True
        elif (n % 2)!=0 or n==0:
            return False
        n=n/2
        result=self.isPowerOfTwo(n)

        if result==True:
            return True
        else:
            return False
