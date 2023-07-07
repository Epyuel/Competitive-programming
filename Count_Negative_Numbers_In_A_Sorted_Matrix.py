class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def countRowNegatives(row:List[int])->int:
            l_pointer=0
            r_pointer=len(row)-1
            count_neg=0
            while l_pointer<=r_pointer:
                mid=(l_pointer+r_pointer)//2
                if row[mid]<0:
                    count_neg+=1
                    r_pointer-=1
                elif row[mid]>=0:
                    l_pointer=mid+1
            return count_neg
        result=0
        for row in grid:
            temp=countRowNegatives(row)
            result+=temp
        return result
