class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersec=[]
        for i in nums1:
            if i not in intersec and i in nums2:
                intersec.append(i)
        return intersec
