class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num = [0] * 60
        n_pairs = 0
        
        for t in time:
            r = t % 60
            s = (60 - r) % 60
            n_pairs += num[s]
            num[r] += 1
        
        return n_pairs
