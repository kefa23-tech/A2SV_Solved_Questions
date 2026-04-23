from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        def dfs(node):

            visited.add(node)
            
            for neighbour in adj_list[node]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        
        
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()

        dfs(source)

        return destination in visited    
