class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        num=0
        i=0
        while i <len(s):
            if i<len(s)-1 and s[i] in "IXC":
                temp=dic.get(s[i]+s[i+1],None)
                if temp!=None:
                    num+=temp
                    i+=2
                    continue
            num+=dic[s[i]]
            i+=1
        return num
