class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lis=[]
        for i in range(len(l)):
            temp=nums[l[i]:r[i]+1]
            temp=sorted(temp)
            diff=temp[1]-temp[0]
            a=False
            for j in range(len(temp)-1):
                if diff!=temp[j+1]-temp[j]:
                    lis.append(False)
                    a=False
                    break
                else:
                    a=True
            if a==True:
                lis.append(True)
        return lis
