class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        highestHour= sorted(dist)[-1]
        val=hour-(len(dist)-1)
        if (val != 0):
            highestHour= math.ceil(max(highestHour,highestHour/(val)))
        l_pointer,r_pointer,mid=1,highestHour,1

        def isLess(dist: List[int], tempHour:float, h: float) -> bool:
            temp=0
            for i in range(len(dist)):
                if i==len(dist)-1:
                    temp+=dist[i]/tempHour
                    break
                temp+= math.ceil(dist[i]/tempHour)
            if temp <= h:
                return True
            return False
        flag=False
        while l_pointer<=r_pointer:
            mid=(l_pointer+r_pointer)//2

            if isLess(dist, mid, hour):
                r_pointer= mid -1
                flag=True
            else:
                flag=False
                l_pointer= mid +1
        if l_pointer!=mid:
            mid=max(l_pointer,mid)
        elif r_pointer!=mid:
            mid=max(r_pointer,mid)
        if isLess(dist,mid,hour):
            return mid
        return -1
