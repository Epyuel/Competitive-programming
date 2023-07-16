class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_freq=collections.Counter(ages)
        def request(i,j):
            if i<= 0.5 * j + 7:
                return False
            if i>j:
                return False
            return True
        req=0
        for i, freq1 in age_freq.items():
            for j, freq2 in age_freq.items():
                if request(i,j):
                    req+=freq1*freq2
                    if i==j:
                        req-=freq1
        return req
