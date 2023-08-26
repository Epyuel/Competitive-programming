class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        islands=0
        dir=[(1,0),(-1,0),(0,1),(0,-1)]

        def isInvalid(row,column):
            return row < 0 or column < 0 or row >=m or column >= n
        
        def dfs(rw,cl):
            if (rw,cl) in visited or grid[rw][cl]=='0':
                return

            visited.add((rw,cl))

            for nr,nc in dir:
                if not isInvalid(rw+nr,cl+nc):
                    dfs(rw+nr,cl+nc)
            
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='1':
                    visited_len = len(visited)
                    dfs(r,c)
                    if visited_len != len(visited):
                        islands+=1
        return islands
