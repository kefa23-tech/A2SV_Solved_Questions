from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True
            
            visited.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(node)
            graph[node] = []
            return True

        graph = defaultdict(list)
     
        for u,v in prerequisites:
       
            graph[u].append(v)
        visited = set()
        
        for crc in range(numCourses):
            if not dfs(crc):
                return False
        
        return True
            