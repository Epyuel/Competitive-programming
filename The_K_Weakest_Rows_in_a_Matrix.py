class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap=[]
        heapq.heapify(heap)
        for i in range(len(mat)):
            l_pointer,r_pointer=0,len(mat[i])-1

            while l_pointer <= r_pointer:
                mid=(r_pointer + l_pointer)//2
                if mat[i][mid]==0:
                    r_pointer=mid-1
                elif mat[i][mid]==1:
                    l_pointer=mid+1

            numOfOne=min(r_pointer,mid)+1
            heapq.heappush(heap,(numOfOne,i))
        lis=[]
        for _ in range(k):
           lis.append(heapq.heappop(heap)[-1])

        return lis
