class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(n//2):   
            ind_rev=n-1-i
            s[i],s[ind_rev]=s[ind_rev],s[i]
