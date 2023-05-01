class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        chars.append([])
        count=1
        while True:
            if (len(chars)-2)<i:
                break
            if chars[i+1]==chars[i]:
                count+=1
            else:
                if count==1:
                    chars[-1]=chars[-1]+list(chars[i])
                else:
                    chars[-1]=chars[-1]+list(chars[i])+list(str(count))
                count=1
            i+=1
        j=0
        for i in chars[-1]:
            chars[j]=i
            j+=1
        return len(chars[-1])
