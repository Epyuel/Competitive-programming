class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot=sum(nums[0:k])
        max_tot= tot
        i,j=0,k-1
        n=len(nums)
        
        while i<n-1 and j<n-1:
            tot=tot-nums[i]+nums[j+1]
            max_tot=max(tot,max_tot)
            i,j=i+1,j+1
        return max_tot/k
