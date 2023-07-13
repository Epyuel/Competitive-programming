class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters=sorted(heaters)

        def findTheShortest(house:int)->int:
            l_pointer,r_pointer,mid=0,len(heaters)-1,0
            min_val=float("inf")
            while l_pointer <= r_pointer:
                mid=(l_pointer+r_pointer)//2
                val=abs(house - heaters[mid])
                if house >= heaters[mid]:
                    l_pointer=mid+1
                else:
                    r_pointer=mid-1
                min_val=min(min_val,val)
            return min_val
        
        max_res=0
        for house in houses:
            temp=findTheShortest(house)
            max_res=max(max_res,temp)
        
        return max_res


