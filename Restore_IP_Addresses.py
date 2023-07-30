class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        validIp=[]
        if len(s)>12:
            return validIp
        def backtrack(ind,points,tempIp):
            if points==4 and ind==len(s):
                validIp.append(tempIp[:-1])
                return
            if points>4:
                return

            for i in range(ind,min(ind+3,len(s))):
                if int(s[ind:i+1])< 256 and (ind==i or s[ind]!="0"):
                    backtrack(i+1, points+1, tempIp + s[ind:i+1] + ".")
        backtrack(0,0,"") 
        return validIp
