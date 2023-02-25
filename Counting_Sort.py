import math,os,random,re,sys
def countingSort(arr):
    lst=[]
    for i in range(100):
        lst.append(0)
    for j in range(n):
        lst[arr[j]]+=1
    return lst
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
