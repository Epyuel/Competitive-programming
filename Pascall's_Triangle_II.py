class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row_prev=[1]
        for i in range(rowIndex):
            if len(row_prev)==1:
                row_prev.append(1)
                continue

            row=[]
            row.append(1)
            for j in range(len(row_prev)-1):
                row.append(row_prev[j] + row_prev[j+1])
            
            row.append(1)
            row_prev=row
        return row_prev
