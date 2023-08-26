class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.backtrack(res,0,[],nums)
        return res
    def backtrack(self,res,start,subset,nums):
        res.append(list(subset))
        for i in range(start,len(nums)):
            subset.append(nums[i])
            self.backtrack(res,i+1,subset,nums)
            subset.pop()
