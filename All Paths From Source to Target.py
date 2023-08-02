class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start=graph[0]
        length=len(graph)
        path=[]
        def helper(branch:List[int],temp:List[int],parent):

            for i in branch:
                temp.append(i)
                if i==length-1:
                    path.append(temp.copy())
                    # continue
                helper(graph[i],temp,i)
                ind=temp.index(parent)
                temp=temp[:ind+1]


        helper(start,[0],0)      
        return path
