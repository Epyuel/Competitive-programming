import math,os,random,re,sys
def countSwaps(a):
    num_swap=0
    for i in a:
        for j in range(n-1):
            if a[j]>a[j+1]:
                num_swap+=1
                (a[j],a[j+1])=(a[j+1],a[j])
    first_item=a[0]
    last_item=a[n-1]
    print(f"Array is sorted in {num_swap} swaps.\nFirst item: {first_item}\nLast item: {last_item}\n")
    return 
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
