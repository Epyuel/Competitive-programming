class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph={}
        visited=set()
        bank= [startGene] + bank
        n=len(bank)

        if endGene not in bank:
            return -1

        def difference(gene1,gene2):
            diff=0
            for i in range(len(gene1)):
                if gene1[i]!=gene2[i]:
                    diff+=1
            return diff
        
        for i in range(n):
            for j in range(i,n):
                if bank[j] == bank[i]:
                    continue
                if difference(bank[i],bank[j])==1:
                    if bank[i] in graph:
                        graph[bank[i]].append(bank[j])
                    else:
                        graph[bank[i]]= [bank[j]]
        if startGene not in graph:
            return -1
        elif graph[startGene]==0:
            return -1
        
        def bfs():
            q= deque([(startGene,0)])
            while q:
                node,level=q.popleft()
                if (node,level) not in visited and node in graph:
                    for k in graph[node]:
                        if k == endGene:
                            return level+1
                        q.append((k,level+1))
                    visited.add((node,level))
            return -1

        return bfs()
