class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combinations=[]
        def backTrack(lis,temp,k):
            if len(temp)==k:
                self.combinations.append(temp.copy())
                return
            for i in range(len(lis)):
                temp.append(lis[i])
                backTrack(lis[i+1:],temp,k)
                temp.pop()            

        backTrack(list(range(1,n+1)),[],k)
        return self.combinations
