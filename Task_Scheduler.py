class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic={}
        for i in range(len(tasks)):
            if tasks[i] in dic:
                dic[tasks[i]]=dic[tasks[i]]+1
            else:
                dic[tasks[i]]=1
        sorted_list=list(sorted(dic.items(),reverse=True,key= lambda x:x[1]))
        k=sorted_list[0][-1]
        t=1
        for i in range(1,len(sorted_list)):
            if sorted_list[i][-1]!=k:
                break
            else:
                t+=1
        total=(k*(n+1))+ t -(n+1)
        x=total-(t*k)
        y=len(tasks)-(t*k)
        sol=max(x,y)
        final=sol+(t*k)
        return final
