class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_zeros = 0
        i = 0
        while 0 in nums:
            nums.remove(0)
            num_zeros += 1
        for i in range(num_zeros):
            nums.append(0)
        return nums
