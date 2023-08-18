class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited=[]
        preval= image[sr][sc]
        def helper(row,column):
            if [row,column] in visited:
                return
            if (row<0 or row > len(image)-1) or (column<0 or column >len(image[0])-1):
                return          
            if image[row][column]!=preval:
                return

            if image[row][column]==preval:
               image[row][column]=color
            visited.append([row,column])
            
            helper(row+1,column)
            helper(row-1,column)
            helper(row,column+1)
            helper(row,column-1)
        
        helper(sr,sc)
        return image
             
