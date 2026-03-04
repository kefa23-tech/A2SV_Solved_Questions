class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        for num in nums:
            if num!=0:
                product*=num
        
        answer = []
        # print(product)
        if nums.count(0)  == 1:
            for num in nums:
                if num == 0:
                    answer.append(product)
                else:
                    answer.append(0)
        elif nums.count(0) > 1:
            return [0]*len(nums)
        else:
            for num in (nums):
                num=product//num
                answer.append(num)
        return answer
        

        return answer