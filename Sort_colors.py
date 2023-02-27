class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            min=nums[i]
            for j  in range(i,len(nums)-1):
                if min > nums[j+1]:
                    min=nums[j+1]
            nums[nums.index(min,i)],nums[i]=nums[i],min
