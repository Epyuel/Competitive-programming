class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        unordered_lst=[]
        min_points=[]
        for i in points:
            dist=sqrt(pow(i[0]-0,2)+pow(i[1]-0,2))
            unordered_lst.append(dist)
        ordered_lst=sorted(unordered_lst)
        for j in range(k):
            temp=ordered_lst[j]
            index=unordered_lst.index(temp)
            unordered_lst[index]=1993
            min_points.append(points[index])
        return min_points
