class Solution:
        def isIsomorphic(self, s: str, t: str) -> bool:
            dic = {}
            l = []
            if len(s) != len(t) :
                return false
            for i in range(0,len(s)) :
                if s[i] in dic.keys():
                    if t[i] == dic[s[i]] :
                        continue
                    else :
                        return False
                else:
                    if t[i] not in l:
                        dic[s[i]] = t[i]
                        l.append(t[i])
                    else :
                        return False    
            return True 
