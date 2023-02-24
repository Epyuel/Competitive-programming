class Solution: 
    def select(self, arr, h):
        select=arr[h]
        for j in range(h,n-1):
            if select>arr[j+1]:
                select=arr[j+1]
        return select
    def selectionSort(self, arr,n):
        for k in range(n):
            a=self.select(arr,k)
            arr[arr.index(a,k)],arr[k]=arr[k],arr[arr.index(a,k)]
        return
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        Solution().selectionSort(arr,n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
