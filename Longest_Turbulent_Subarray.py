class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l_pointer=0
        max_turnulence=1
        count=1
        flag=2
        for r_pointer in range(len(arr)-1):
            if arr[r_pointer] < arr[r_pointer+1] and (flag==0 or flag==2):
                flag=1
                count+=1
            elif arr[r_pointer] > arr[r_pointer+1] and (flag==1 or flag==2):
                flag=0
                count+=1
            else:
                l_pointer=r_pointer
                if arr[r_pointer]!=arr[r_pointer+1]:
                    count=2
                else:
                    count=1
            max_turnulence= max(max_turnulence,count)

        return max_turnulence
