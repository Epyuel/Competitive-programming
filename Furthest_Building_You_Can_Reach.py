class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        index=0
        for i in range(len(heights)-1):
            if heights[i+1]-heights[i]<=0 :
                index+=1
            elif heights[i+1]-heights[i]<=bricks:
                bricks-= heights[i+1]-heights[i]
                heapq.heappush(heap,-1*(heights[i+1]-heights[i]))
                index+=1
            elif (heights[i+1]-heights[i]>bricks) and ladders:
                if heap and -1*heap[0] > heights[i+1]-heights[i]:
                    temp= -1*heapq.heappop(heap)
                    bricks+=temp
                    ladders-=1 

                    bricks-= heights[i+1]-heights[i]
                    heapq.heappush(heap,-1*(heights[i+1]-heights[i]))
                else:
                    ladders-=1
                index+=1
            elif (not ladders) and bricks < heights[i+1]-heights[i]:
                break

        return index
            
