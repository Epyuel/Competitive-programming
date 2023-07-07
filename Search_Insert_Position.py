class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
         l_pointer=0
         r_pointer=len(nums)-1

         
         while l_pointer <= r_pointer:
            mid=(l_pointer + r_pointer)//2
            if nums[l_pointer]==target:
                return l_pointer
            elif nums[mid]==target:
                return mid
            elif nums[r_pointer]==target:
                return r_pointer
            elif nums[mid]>target:
                r_pointer=mid
            elif nums[mid]<target:
                l_pointer=mid 
                
            if (l_pointer==r_pointer-1 or l_pointer==r_pointer):
                if nums[r_pointer]<target:
                    return r_pointer+1
                elif nums[l_pointer]>target:
                    return l_pointer
                else:
                    return l_pointer+1
