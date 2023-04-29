class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        num=nums[-k:]+nums[:len(nums)-k]
        for i in range(len(nums)):
            nums[i]=num[i]
