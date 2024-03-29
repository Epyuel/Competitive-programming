class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def dfs(source, output):
            least_quiet = source
            for neighbor in graph[source]:
                if output[neighbor] is None:
                    dfs(neighbor, output)
                least_quiet = min(least_quiet, output[neighbor], key=lambda x: quiet[x])
            output[source] = least_quiet

        
        n = len(quiet)
        graph = [set() for i in range(n)]
        for relation in richer:
            graph[relation[1]].add(relation[0])
        output = [None for i in range(n)]
        for person in range(n):
            if output[person] is None:
                dfs(person,output)
        return output
         
