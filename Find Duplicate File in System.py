
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        contents = defaultdict(list)

        for path in paths:
            
            path = path.split()
            root = path[0]

            for file in path[1:]:
                file_name,_,content = file.partition("(")
                contents[content].append(root +'/' + file_name)
        ans = []
        for file in contents.values():
            if len(file) > 1:
                ans.append(file)   
        return ans         

        
