class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums=list(map(lambda x: -1* x,nums))
        heapq.heapify(neg_nums)

        for i in range(k-1):
            heapq.heappop(neg_nums)

        return -1*heappop(neg_nums)
