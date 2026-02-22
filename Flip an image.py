class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(image)):
            row = image[i]
            row = row[::-1]
            image[i] = row
        for i in range(len(image)):
            row = image[i]
            for j in range(len(row)):
                if row[j] == 0:
                    row[j] = 1
                else:
                    row[j] = 0
            image[i] = row
        return image
