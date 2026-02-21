class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        size = len(arr)

        for i in range(size,1,-1):
            max_idx = arr.index(i)

            if max_idx == size - 1:
                continue
            elif max_idx != 0:
                res.append(max_idx + 1)
                arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
            
            res.append(i)
            arr[:i] = arr[:i][::-1]
        return res
