class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        curr_state = [0, 0, 0] 
        def determiner(nums, curr_state):
            if len(nums) == 0:
                return curr_state[0] >= curr_state[1]
            if len(nums) == 1:
                if curr_state[2] == 0:
                    return curr_state[0] + nums[0] >= curr_state[1]
                else:
                    return curr_state[0] >= curr_state[1] + nums[0]
            if curr_state[2] == 0:
                return determiner(nums[1:], [curr_state[0] + nums[0], curr_state[1], 1]) or determiner(nums[:-1], [curr_state[0] + nums[-1], curr_state[1], 1])
            else:
                return determiner(nums[1:], [curr_state[0], curr_state[1] + nums[0], 0]) and determiner(nums[:-1], [curr_state[0], curr_state[1] + nums[-1], 0])
            return res
        return determiner(nums, curr_state)
