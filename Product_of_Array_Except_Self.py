class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProduct= [1,nums[0]]
        for i in range(1,len(nums)):
            prefProduct.append(prefProduct[-1]*nums[i])
        
        postProduct= [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            postProduct.append(postProduct[-1]*nums[i])

        postProduct=postProduct[::-1]+[1]

        soln=[]
        for i in range(len(nums)):
            soln.append(prefProduct[i]*postProduct[i+1])
        return soln
