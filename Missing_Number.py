class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if nums[0]!=0:
            return 0
        elif nums[-1]!=len(nums):
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]-1:
                return nums[i]+1
