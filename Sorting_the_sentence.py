class Solution:
    def sortSentence(self, s: str) -> str:
        unsorted_lst=s.split()
        sorted_lst=[]
        for j in range(len(unsorted_lst)):
            sorted_lst.append(0)
        for i in unsorted_lst:
            index=int(i[-1])-1
            sorted_lst[index]=i   
        for k in range(len(sorted_lst)):
            a=sorted_lst[k][0:-1]
            sorted_lst[k]=a
        return (" ".join(sorted_lst))
