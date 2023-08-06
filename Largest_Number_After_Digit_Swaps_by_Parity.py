class Solution:
    def largestInteger(self, num: int) -> int:
        even_heap=[]
        odd_heap=[]
        heapq.heapify(even_heap)
        heapq.heapify(odd_heap)

        lis=[]
        str_num=str(num)
        for i in str_num:
            if int(i)%2==0:
                heapq.heappush(even_heap,-1*int(i))
            else:
                heapq.heappush(odd_heap,-1*int(i))

        for i in str_num:
            if int(i)%2==0:
                even=-1*heapq.heappop(even_heap)
                lis.append(str(even))
            else:
                odd=-1*heapq.heappop(odd_heap)
                lis.append(str(odd))
        return int("".join(lis))

            


            
