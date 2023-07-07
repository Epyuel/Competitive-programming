class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        sum=count = 0
        freq = 1
        hash[sum] = freq
        for i in nums:
            sum = sum+i
            if sum-k in hash.keys():
                count = count+hash[sum-k]
            if sum not in hash.keys():
                hash[sum] = freq
            else:
                hash[sum] = hash[sum]+1
        return count
