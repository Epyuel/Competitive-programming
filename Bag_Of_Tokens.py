class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score,maxim=0,0
        tokens=sorted(tokens)
        i,j=0,len(tokens)-1
        while True:
            flag=False
            if j<i:
                break
            if tokens[i]<=power:
                score+=1
                power-=tokens[i]
                i+=1
                flag=True
            elif tokens[i]>power and score>=1:
                score-=1
                power+=tokens[j]
                j-=1
                flag=True
            if score>=maxim:
                maxim=score
            if not(flag):
                break
        return maxim
