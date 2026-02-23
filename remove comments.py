class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        res = []
      
        inblock = False

        for line in source:
            i = 0
            if not inblock:
                code = []
            while i < len(line):
        #check if a multiple line cmnt started and the starter is not in block              
                
                char = line[i]
                if line[i:i+2] == "/*" and not inblock:
                    inblock = True
                    i+=1
        #check if a multiple line cmnt is ending
                elif line[i:i+2] == "*/" and inblock:
                    inblock  = False
                    i+=1
        #check for a single line cmnt
                elif line[i:i+2] == "//" and not inblock:
                    break
        # if a the char isnot inblock and not a single line comment

                elif not inblock:
                    code.append(char)
                i+=1  
            # 
            if code and not inblock:
                res.append("".join(code))
        return res











