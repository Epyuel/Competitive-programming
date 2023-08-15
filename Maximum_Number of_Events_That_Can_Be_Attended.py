class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key= lambda x:x[0])
        max_num_days=max([event[1] for event in events])

        day,index,res=0,0,0
        heap=[]
        while day <= max_num_days:
            while index< len(events) and events[index][0]<=day:
                heapq.heappush(heap,events[index][1])
                index+=1
            
            while heap and heap[0]<day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                res+=1
            day+=1

        return res
