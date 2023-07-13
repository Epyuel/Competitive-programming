class Solution:
    def firstUniqChar(self, s: str) -> int:
        s,temp = list(s),[]
        for i in range(0,len(s)):
            if s[i] in s[i+1:] or s[i] in temp:
                temp.append(s[i])
            else:
                return i
        return -1
