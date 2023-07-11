class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        for i in arr:
            res.append((abs(i-x),i))
        sorted_res=sorted(res,key=lambda x:x[0])
        return sorted(list(map(lambda x: x[-1],sorted_res[:k])))
