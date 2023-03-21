class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            index=nums2.index(i)
            flag=False
            for j in range(index,len(nums2)):
                if nums2[index]<nums2[j]:
                    ans.append(nums2[j])
                    flag=True
                    break
            if not(flag):
                ans.append(-1)
        return ans
