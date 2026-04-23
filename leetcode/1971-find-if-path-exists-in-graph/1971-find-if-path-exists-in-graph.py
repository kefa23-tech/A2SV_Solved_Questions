from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        def dfs_iterative(start):

            stack = [start]

            while stack:
                node = stack.pop()

                if node not in visited:
                    visited.add(node)
                    for neighbour in adj_list[node]:
                        stack.append(neighbour) 
        
        
        
        adj_list = defaultdict(list)

        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()

        dfs_iterative(source)

        return destination in visited    
