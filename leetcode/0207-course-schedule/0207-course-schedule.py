from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
 
        def kahns_algo(num_nodes,edges):

            adj = {i:[] for i in range(num_nodes)}
            indegree = [0] * num_nodes

            for u,v in edges:
                adj[u].append(v)
                indegree[v]+=1
            

            queue = deque([i for i in range(num_nodes) if indegree[i] == 0 ])
            courses = 0
            while queue:
                u = queue.popleft()
                courses+=1

                for nei in adj[u]:
                    indegree[nei]-=1
                    if indegree[nei] == 0:
                        queue.append(nei)
            
            return courses

        taken = kahns_algo(numCourses,prerequisites)

        return taken == numCourses






























        # def dfs(node):

        #     if node in visited:
        #         return False
        #     if graph[node] == []:
        #         return True
        #     visited.add(node)
        #     for nei in graph[node]:
        #         if not dfs(nei):
        #             return False

        #     visited.remove(node)
        #     graph[node] = []

        #     return True




        # graph = defaultdict(list)

        # for u,v in prerequisites:
        #     graph[u].append(v)
        # visited = set()
        # for node in range(numCourses):
        #     if not dfs(node):
        #         return False


        # return True    




















        # def dfs(node):
        #     if node in visited:
        #         return False
        #     if graph[node] == []:
        #         return True
            
        #     visited.add(node)

        #     for neighbor in graph[node]:
        #         if not dfs(neighbor):
        #             return False
            
        #     visited.remove(node)
        #     graph[node] = []
        #     return True

        # graph = defaultdict(list)
     
        # for u,v in prerequisites:
       
        #     graph[u].append(v)
        # visited = set()
        
        # for crc in range(numCourses):
        #     if not dfs(crc):
        #         return False
        
        # return True
            