import math,os,random,re,sys
def insertionSort1(n, arr):
    last=arr[n-1]
    for i in range(n-2,-1,-1):
        if i==0 and last<arr[0]:
            arr[i+1]=arr[i]
            temp=map(str,arr)
            print(" ".join(temp))
            arr[i]=last
            temp=map(str,arr)
            print(" ".join(temp))
            
        elif last<arr[i]:
            arr[i+1]=arr[i]
            temp=map(str,arr)
            print(" ".join(temp))
        else:
            arr[i+1]=last
            temp=map(str,arr)
            print(" ".join(temp))
            break
    return
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
