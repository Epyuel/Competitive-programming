class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lis=[]
        i,j,temp=0,1,0
        while True:
            if i>len(s)-1:
                break
            if s[i] in s[j:]:
                j+=1
            else:
                if i+1==j:
                    lis.append(len(s[temp:j]))
                    temp=i+1
                i+=1
        return lis
