#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a = Counter(a)
        b = Counter(b)
        for k in b:
            if a[k] < b[k]:
                return False
        return True

    
    
