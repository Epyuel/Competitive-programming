class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq={}
        for edge in edges:
            if edge[0] not in freq:
                freq[edge[0]]=1
            else:
                freq[edge[0]]+=1
            if edge[1] not in freq:
                freq[edge[1]]=1
            else:
                freq[edge[1]]+=1
        maxVal=[0,-1*float("inf")]
        for i in freq:
            if freq[i]>maxVal[1]:
                maxVal=[i,freq[i]]
        return maxVal[0]

        
            
