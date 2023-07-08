class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        l_pointer = s = 0
        for r_pointer, num in enumerate(nums):
            s += num
            while s >= target:
                s -= nums[l_pointer]
                res = min(res, r_pointer - l_pointer + 1)
                l_pointer += 1
        if res > len(nums):
            return 0
        else:
            return res
