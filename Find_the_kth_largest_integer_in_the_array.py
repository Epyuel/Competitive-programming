class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_lst=map(int,nums)
        int_lst=sorted(int_lst,reverse=True)
        return str(int_lst[k-1])
