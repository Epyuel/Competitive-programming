class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l_pointer=max_length=cost=0
        for r_pointer in range(len(s)):
            cost+=abs(ord(s[r_pointer])-ord(t[r_pointer]))

            while cost>maxCost:
                cost-=abs(ord(s[l_pointer])-ord(t[l_pointer]))
                l_pointer+=1
            
            max_length=max(max_length,(r_pointer - l_pointer)+1)

        return max_length
