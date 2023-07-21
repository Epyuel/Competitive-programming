class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.helper(nums,[])
        return self.res
    def helper(self,temp,path):
        if not temp:
            self.res.append(path)
        for j in range(len(temp)):
            self.helper(temp[:j]+temp[j+1:],path+[temp[j]])
        
    
