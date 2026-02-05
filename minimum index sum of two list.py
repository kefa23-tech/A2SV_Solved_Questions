class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        list3 = set(list1) & set(list2)
        res = []
        filterer = []
     
        for word in list3:
            idx1 = list1.index(word)
            idx2 = list2.index(word)

            filterer.append([idx1+idx2,word])
        filterer.sort()
        minn = filterer[0][0]

        for pair in filterer:
            if pair[0] == minn:
                res.append(pair[1])
            

        return res

