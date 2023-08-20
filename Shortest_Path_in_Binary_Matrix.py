class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dir=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        if n==1 and not grid[0][0]:
            return 1

        def isInvalid(row,column):
            return row<0 or column<0 or row>=n or column>=n

        

        def bfs():
            visited=set()
            res=2
            if grid[0][0]:
                return -1
            q=deque([(0,0)])
            while q:
                for i in range(len(q)):
                    r,c= q.popleft()
                    for rw,cl in dir:
                        if isInvalid(rw+r,cl+c) or grid[rw+r][cl+c] or (rw+r,cl+c) in visited:
                            continue
                        if (rw+r,cl+c)==(n-1,n-1):
                            return res
                        q.append((rw+r,cl+c))
                        visited.add((rw+r,cl+c))
                res+=1
            return -1
        return bfs()
