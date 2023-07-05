class Solution:
    def countGoodNumbers(self, n: int) -> int:
        result=1
        if n%2!=0:
            result=5
        result=(self.power(20,n//2)*result)%(pow(10,9)+7)
        return result

    def power(self,b,e):
        if e==0:
            return 1
        res=self.power(b,e//2)%(pow(10,9)+7)
        if e%2==0:
            return res*res
        else:
            return res*res*b
